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

from display import DataDisplay
from login import LoginWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        self.dataDisplay = DataDisplay()
        self.windowStack.addWidget(self.dataDisplay)
        self.windowStack.setCurrentIndex(1)

    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.dataDisplay.fileWriter.writeEOF("outputName")
            self.close()


# start app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
