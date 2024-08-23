# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
import queue
import threading

from groundStation.FileWriter import FileWriter
from groundStation.SerialCommunicator import SerialCommunicator
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTextBrowser



class RawText(QTextBrowser):
    def __init__(self):
        super().__init__()

        # object instantiation
        self.timer = QTimer(self)
        self.fileWriter = FileWriter()
        self.sc = SerialCommunicator("/dev/serial0", 9600)

        # connections and variable instantiations
        self.timer.timeout.connect(self.dataOut)
        self.timerRunning = False
        self.iterations = 0
        self.q = queue.Queue()

        # setup for before run
        self.setPlainText("This is the starting message!")
        self.displayLoop()
        listenThread = threading.Thread(target=self.sc.start, args=[self.q])
        listenThread.start()

    def displayLoop(self):
        if not self.timer.isActive():
            self.timer.stop()

        self.timer.start(50)

    def dataOut(self):
        message = str(self.q.get())
        if not (self.iterations < 20):
            self.appendText(message)
            self.iterations = 0

        self.fileWriter.addToFile(str(self.q.get()) + str(self.iterations) + "\n")
        self.iterations += 1

    def appendText(self, message):
        self.append(message)
