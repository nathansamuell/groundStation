# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
from groundStation.DataDisplay import DataDisplay
from groundStation.LoginWindow import LoginWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.isDisplayOn = False
        self.windowStack = QStackedLayout()
        self.loginWindow = LoginWindow()
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)
        self.loginWindow.numpad.loginFailure.connect(self.loginFailure)

        self.windowStack.addWidget(self.loginWindow)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800, 480)
        # self.showFullScreen()

    def loginSuccess(self):
        self.isDisplayOn = True
        self.dataDisplay = DataDisplay()
        self.windowStack.addWidget(self.dataDisplay)
        self.windowStack.setCurrentIndex(1)

    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.isDisplayOn:
                self.dataDisplay.fileWriter.writeEOF("outputName")

            # stops the listening thread and closes the app
            self.dataDisplay.sc.stop()
            self.close()
