# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
import sys
import unittest
from unittest.mock import patch
from PyQt5.QtTest import QSignalSpy

from groundStation.MainWindow import MainWindow, WindowStatus
from groundStation.Numpad import Numpad

class TestMainWindow(unittest.TestCase):
    def test_initial_state(self):
        mainWindow = MainWindow()
        stateListener = QSignalSpy(mainWindow.statusSignal)
        self.assertEqual(len(stateListener), 1) # check for signal emission
        self.assertEqual(mainWindow.status, WindowStatus.LOGIN) # check for the correct signal
        stateListener.clear()

    @patch("os.getenv")
    def test_tsm_login_success(self, mock_env):
        mainWindow = MainWindow()
        stateListener = QSignalSpy(mainWindow.statusSignal)
        mock_env.return_value = "1234"
        mainWindow.loginWindow.numpad.loginPin = "1234"
        mainWindow.loginWindow.numpad.authenticate()
        self.assertEqual(len(stateListener), 1)  # only one signal emitted!
        self.assertEqual(mainWindow.status, WindowStatus.RAW_TEXT)  # TODO: change to default view once implemented
        stateListener.clear()
