// SRAD Avionics Ground Software for AIAA UH
//
// Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
// Licensed under the MIT License
//
// More information on the MIT license as well as a complete copy
// of the license can be found here: https://choosealicense.com/licenses/mit/
// All above text must be included in any restribution.

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"

	"groundStation-OS-autostart/commands"

	"github.com/charmbracelet/bubbles/help"
	"github.com/charmbracelet/bubbles/key"
	"github.com/charmbracelet/bubbles/spinner"
	"github.com/charmbracelet/bubbles/timer"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

// styles go below:
var (
	selectedStyle = lipgloss.NewStyle().
		Foreground(lipgloss.Color("78")).
		Bold(true) // Example styling
)

const timeout = time.Second * 1

type viewState int

const (
	Loading viewState = iota
	Commands
	NoCommands
)

type command struct {
	sudo    bool
	command string
	args    []string
	name    string
	order   int
}

type model struct {
	choices         *[]command
	cursor          int
	selected_option map[int]int
	keys            keyMap
	help            help.Model
	totalOrder      int
	loading         spinner.Model
	loadTimer       timer.Model
	displayState    viewState
}

// the struct changes the key behavior and implements help menu!
type keyMap struct {
	Up      key.Binding
	Down    key.Binding
	Select  key.Binding
	Execute key.Binding
	Help    key.Binding
	Quit    key.Binding
}

var keys = keyMap{
	Up: key.NewBinding(
		key.WithKeys("up", "k"),
		key.WithHelp("↑/k", "move up"),
	),
	Down: key.NewBinding(
		key.WithKeys("down", "j"),
		key.WithHelp("↓/j", "move down"),
	),
	Select: key.NewBinding(
		key.WithKeys(" "),
		key.WithHelp("␣/space", "select"),
	),
	Execute: key.NewBinding(
		key.WithKeys("enter"),
		key.WithHelp("↵/enter", "execute"),
	),
	Help: key.NewBinding(
		key.WithKeys("h"),
		key.WithHelp("h", "toggle help"),
	),
	Quit: key.NewBinding(
		key.WithKeys("q", "esc", "ctrl+c"),
		key.WithHelp("q", "quit"),
	),
}

func (k keyMap) ShortHelp() []key.Binding {
	return []key.Binding{k.Help, k.Quit}
}

func (k keyMap) FullHelp() [][]key.Binding {
	return [][]key.Binding{
		{k.Up, k.Down, k.Select, k.Execute},
		{k.Help, k.Quit},
	}
}

func generateCommandChoices() *[]command {
	var commandArray []command

	// below are the choices that always exist
	LAUNCH_GS := command{
		sudo:    false,
		command: "startx /bin/bash -c \"python3 -m groundStation\"",
		name:    "run groundStation",
	}

	UPDATE_OS := command{
		sudo:    true,
		command: "apt update",
		name:    "refresh apt",
	}

	UPGRADE_OS := command{
		sudo:    true,
		command: "apt upgrade -y",
		name:    "upgrade packages",
	}

	REBOOT := command{
		sudo:    false,
		command: "reboot",
		name:    "reboot pi",
	}

	POWEROFF := command{
		sudo:    false,
		command: "poweroff",
		name:    "shutdown pi",
	}
	OTHER := command{
		sudo: true,
		name: "other (jump to terminal)",
		args: []string{},
	}

	commandArray = append(commandArray, LAUNCH_GS)
	commandArray = append(commandArray, UPDATE_OS)
	commandArray = append(commandArray, UPGRADE_OS)
	commandArray = append(commandArray, REBOOT)
	commandArray = append(commandArray, POWEROFF)
	commandArray = append(commandArray, OTHER)

	return &commandArray // returns a pointer to save memory -- predefined commands are the same!
}

func createInitialModel() model {
	return model{
		choices:         generateCommandChoices(),
		help:            help.New(),
		keys:            keys,
		selected_option: make(map[int]int),
		totalOrder:      0,
		loading:         spinner.NewModel(),
		loadTimer:       timer.NewWithInterval(timeout, time.Millisecond),
		displayState:    Loading,
	}
}

// bubbletea functions
func (m model) Init() tea.Cmd {
	cmd1 := m.loading.Tick
	cmd2 := m.loadTimer.Init()

	return tea.Batch(cmd1, cmd2)
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	cmd := tea.EnterAltScreen
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch {
		case key.Matches(msg, m.keys.Quit):
			return m, tea.Quit

		case key.Matches(msg, m.keys.Up):
			if m.cursor > 0 {
				m.cursor--
			}

		case key.Matches(msg, m.keys.Down):
			if m.cursor < len(*m.choices)-1 {
				m.cursor++
			}

		case key.Matches(msg, m.keys.Select):
			_, ok := m.selected_option[m.cursor]
			if ok {
				delete(m.selected_option, m.cursor)
				m.totalOrder--
				(*m.choices)[m.cursor].order = m.totalOrder
			} else {
				m.totalOrder++
				(*m.choices)[m.cursor].order = m.totalOrder
				m.selected_option[m.cursor] = m.totalOrder
			}

		case key.Matches(msg, m.keys.Help):
			m.help.ShowAll = !m.help.ShowAll
		}
	case spinner.TickMsg:
		var cmd tea.Cmd
		m.loading, cmd = m.loading.Update(msg)
		return m, cmd

	case timer.TickMsg:
		var cmd tea.Cmd
		m.loadTimer, cmd = m.loadTimer.Update(msg)
		return m, cmd

	case timer.TimeoutMsg:
		return m, commands.CheckForPersistingCommands

	case commands.FoundCommands:
		if !msg.Commands {
			m.displayState = NoCommands
		} else {
			m.displayState = Commands
		}
	}

	return m, cmd
}

func (m model) LoadingView() string {
	s := m.loading.View() + " Loading GroundStation Launcher..."
	// s += m.loadTimer.View()
	return s
}

func (m model) CommandsView() string {
	s := m.loading.View() + " Executing remaining commands..."
	return s
}

func (m model) NoCommandsView() string {
	// initial header!
	s := "Welcome to GroundStation!\n\n"
	s += "Options below:\n\n"

	for i, command := range *m.choices {

		// Is the cursor pointing at this choice?
		cursor := " " // no cursor
		if m.cursor == i {
			cursor = ">" // cursor!
		}

		// Is this choice selected?
		checked := selectedStyle.Render(" ") // not selected
		if _, ok := m.selected_option[i]; ok {
			checked = selectedStyle.Render(strconv.Itoa(command.order))
		}

		s += fmt.Sprintf("%s [%s] Option %d: %s \n", cursor, checked, i, command.name)
	}

	helpView := m.help.View(m.keys)
	height := 15 - strings.Count(s, "\n") - strings.Count(helpView, "\n")

	return s + strings.Repeat("\n", height) + helpView
}

func (m model) View() string {
	switch m.displayState {
	case Loading:
		return m.LoadingView()
	case Commands:
		return m.CommandsView()
	case NoCommands:
		return m.NoCommandsView()
	}

	return "Error: press q to quit"
}

func main() {
	p := tea.NewProgram(createInitialModel())
	if _, err := p.Run(); err != nil {
		fmt.Printf("Alas, there's been an error: %v", err)
		os.Exit(1)
	}

}
