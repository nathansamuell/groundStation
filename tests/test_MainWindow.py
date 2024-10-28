# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
import unittest

from groundStation.MainWindow import MainWindow, WindowStatus
from PyQt5.QtTest import QSignalSpy
from PyQt5.QtWidgets import QApplication


class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testApp = QApplication([])

    def setUp(self):
        self.mainWindow = MainWindow()
        self.stateListener = QSignalSpy(self.mainWindow.statusSignal)

    def test_initial_state(self):
        self.mainWindow.initGUI()
        self.assertEqual(len(self.stateListener), 1)  # check for signal emission
        self.assertEqual(
            self.mainWindow.status, WindowStatus.LOGIN
        )  # check for the correct signal

    def test_tsm_login_success(self):
        self.mainWindow.statusSignal.emit(WindowStatus.RAW_TEXT)
        self.assertEqual(len(self.stateListener), 1)  # only one signal emitted!
        self.assertEqual(
            self.mainWindow.status, WindowStatus.RAW_TEXT
        )  # TODO: change to default view once implemented

    def tearDown(self):
        self.mainWindow.close()
        self.testApp.processEvents()


if __name__ == "__main__":
    unittest.main()
