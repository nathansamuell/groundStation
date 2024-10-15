package commands

import (
	tea "github.com/charmbracelet/bubbletea"
)

func CheckForPersistingCommands() tea.Msg {
	msg := FoundCommands{Commands: false}

	return msg
}

type FoundCommands struct {
	Commands bool
}
