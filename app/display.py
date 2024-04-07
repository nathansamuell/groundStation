# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
from fileWriter import FileWriter
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTextBrowser


class DataDisplay(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.iterations = 0
        self.timer = QTimer(self)
        self.fileWriter = FileWriter()
        self.timer.timeout.connect(self.dataOut)
        self.timerRunning = False
        self.setPlainText("This is the starting message!")
        self.displayLoop()

    def displayLoop(self):
        if not self.timer.isActive():
            self.timer.stop()

        self.timer.start(1000)

    def dataOut(self):
        self.appendText()
        self.fileWriter.addToFile(
            "This Message is appended! " + str(self.iterations) + "\n"
        )
        self.iterations += 1

    def appendText(self):
        self.append("This message is appended!")
