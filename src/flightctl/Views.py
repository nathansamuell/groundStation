# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
import importlib.resources as resources  # used for image handling
import os
import queue
import threading

# app class/qt imports
from dotenv import load_dotenv
from flightctl.FileWriter import FileWriter
from flightctl.Numpad import Numpad
from flightctl.SerialCommunicator import SerialCommunicator
from PyQt5.QtCore import QTimer

# qt imports
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


# aiaa image path finder
def getLogoPath():
    with resources.path(__package__, "cropped-aiaaweblogo-2.png") as path:
        return str(path)


# The Login Window with the password etc
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        aiaaLogo = QLabel()
        aiaaLogo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.enterPinText = QLabel("       Enter PIN:")
        self.enterPinText.setFixedHeight(150)
        font = QFont()
        font.setPointSize(16)
        self.enterPinText.setFont(font)

        spacerL = QSpacerItem(240, QSizePolicy.Ignored)
        spacerR = QSpacerItem(240, QSizePolicy.Ignored)

        aiaaLogo.setPixmap(QPixmap(getLogoPath()))
        self.numpad = Numpad()

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()

        layout3.addItem(spacerL)
        layout3.addWidget(self.enterPinText)
        layout3.addItem(spacerR)

        layout2.addLayout(layout3)
        layout2.addWidget(self.numpad)
        layout1.addWidget(aiaaLogo)
        layout1.addLayout(layout2)

        # set the layout to the window
        self.setLayout(layout1)


# the barebones view
#
# currently the default until I finish the new default view.
# a list of those components will be left below later on
#
#
#
# other view ideas:
#   --gps info/location info
#   --flight stage/status
#   --data transmission indicator?
#   --send message to the rocket in the future maybe?
class RawText(QTextBrowser):
    def __init__(self):
        super().__init__()

        # object instantiation
        self.timer = QTimer(self)
        self.fileWriter = FileWriter()
        # find the right serial port
        load_dotenv()
        mock = os.getenv("MOCK_SERIAL")
        if mock == "True":
            port = os.getenv("MOCK_SPORT_GS")
            self.sc = SerialCommunicator(port, 9600)
        else:
            port = os.getenv("SERIAL_PORT")
            self.sc = SerialCommunicator(port, 9600)

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

        self.timer.start(10)

    def dataOut(self):
        try:
            message = str(self.q.get(timeout=1))

        except queue.Empty as e:
            message = "No data received!" + str(e)

        # if not self.q:
        #     message = "No data received..."
        # else:
        #     message = str(self.q.get())
        if not (self.iterations < 20):
            self.appendText(message)
            self.iterations = 0

        self.fileWriter.addToFile(
            str(message)  # noqa: E128
            #  + str(self.iterations)  # noqa: E128
            + "\n"
        )  # noqa: E124
        self.iterations += 1

    def appendText(self, message):
        self.append(message)
