# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
from enum import Enum

from flightctl.Views import LoginWindow, RawText
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget


class WindowStatus(Enum):
    LOGIN = 0
    DEFAULT = 1
    FLIGHT_TIME = 2
    RAW_TEXT = 3


class MainWindow(QMainWindow):
    # view status signal
    statusSignal = pyqtSignal(WindowStatus)

    def __init__(self):
        super().__init__()

        self.isDisplayOn = False
        self.windowStack = QStackedLayout()
        self.loginWindow = LoginWindow()
        self.statusSignal.connect(self.updateStatus)
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)
        self.loginWindow.numpad.loginFailure.connect(self.loginFailure)

    def initGUI(self):
        self.windowStack.addWidget(self.loginWindow)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800, 480)
        self.statusSignal.emit(WindowStatus.LOGIN)
        # self.showFullScreen()

    def updateStatus(self, status):
        if status == WindowStatus.RAW_TEXT:
            # print("update status method called")
            self.status = WindowStatus.RAW_TEXT
            self.windowStack.setCurrentIndex(1)
        elif status == WindowStatus.LOGIN:
            # print("login window status called")
            self.status = WindowStatus.LOGIN
            self.windowStack.setCurrentIndex(0)

    def loginSuccess(self):
        self.isDisplayOn = True
        self.rawText = RawText()
        self.windowStack.addWidget(self.rawText)
        self.statusSignal.emit(WindowStatus.RAW_TEXT)

    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.statusSignal.emit(WindowStatus.DEFAULT)

        elif event.key() == Qt.Key_2:
            self.statusSignal.emit(WindowStatus.FLIGHT_TIME)

        elif event.key() == Qt.Key_3:
            self.statusSignal.emit(WindowStatus.RAW_TEXT)

        elif event.key() == Qt.Key_Escape:
            # stops the listening thread and closes the app
            if self.status == WindowStatus.RAW_TEXT:
                self.rawText.sc.stop()
                self.rawText.fileWriter.writeEOF("outputName")

            self.close()
