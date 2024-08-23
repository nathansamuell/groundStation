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
from groundStation.Views import RawText
from groundStation.LoginWindow import LoginWindow
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget


class windowStatus(Enum):
    DEFAULT = 1
    FLIGHT_TIME = 2
    RAW_TEXT = 3


class MainWindow(QMainWindow):
    # view status signal
    statusSignal = pyqtSignal(windowStatus)

    def __init__(self):
        super().__init__()

        self.isDisplayOn = False
        self.windowStack = QStackedLayout()
        self.loginWindow = LoginWindow()
        self.statusSignal.connect(self.updateStatus)
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)
        self.loginWindow.numpad.loginFailure.connect(self.loginFailure)

        self.windowStack.addWidget(self.loginWindow)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800, 480)
        # self.showFullScreen()

    def updateStatus(self, status):
        if status == windowStatus.RAW_TEXT:
            print("update status method called")
            self.windowStack.setCurrentIndex(1)

    def loginSuccess(self):
        self.isDisplayOn = True
        self.rawText = RawText()
        self.windowStack.addWidget(self.rawText)
        self.statusSignal.emit(windowStatus.RAW_TEXT)


    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.statusSignal.emit(windowStatus.DEFAULT)

        elif event.key() == Qt.Key_2:
            self.statusSignal.emit(windowStatus.FLIGHT_TIME)

        elif event.key() == Qt.Key_3:
            self.statusSignal.emit(windowStatus.RAW_TEXT)

        elif event.key() == Qt.Key_Escape:
            if self.isDisplayOn:
                self.rawText.fileWriter.writeEOF("outputName")

            # stops the listening thread and closes the app
            self.rawText.sc.stop()
            self.close()
