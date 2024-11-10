# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
import pytest
from flightctl.MainWindow import MainWindow, WindowStatus
from PyQt5.QtTest import QSignalSpy
from PyQt5.QtWidgets import QApplication


@pytest.fixture(scope="module")
def test_app():
    app = QApplication([])
    yield app


@pytest.fixture
def main_window(test_app):
    window = MainWindow()
    yield window
    window.close()


def test_initial_state(main_window):
    state_listener = QSignalSpy(main_window.statusSignal)
    main_window.initGUI()
    assert len(state_listener) == 1  # check for signal emission
    assert main_window.status == WindowStatus.LOGIN  # check for the correct signal


def test_tsm_login_success(main_window):
    state_listener = QSignalSpy(main_window.statusSignal)
    main_window.statusSignal.emit(WindowStatus.RAW_TEXT)
    assert len(state_listener) == 1  # only one signal emitted!
    assert (
        main_window.status == WindowStatus.RAW_TEXT
    )  # TODO: change to default view once implemented
