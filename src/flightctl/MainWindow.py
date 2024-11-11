# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.


# imports
import os

from enum import Enum
from dotenv import load_dotenv

from flightctl.Views import LoginWindow, RawText
from flightctl.FileWriter import FileWriter
from flightctl.Numpad import Numpad
from flightctl.SerialCommunicator import SerialCommunicator
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget


class WindowStatus(Enum):
    INIT = 0
    LOGIN = 1
    DEFAULT = 2
    RAW_TEXT = 3
    FC_STATUS = 4  # this view shows us status updates from rocket components


class MainWindow(QMainWindow):
    # view status signal
    statusSignal = pyqtSignal(WindowStatus)

    # overrode initial constructor
    def __init__(self):
        super().__init__()

        # window level setup
        self.isDisplayOn = False
        self.windowStack = QStackedLayout()
        self.statusSignal.connect(self.updateStatus)
        self.updateStatus(WindowStatus.INIT)
        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800, 480)
        # self.showFullScreen()

        # initialize modules
        self.initGUI()
        self.initNP()
        self.initFW()
        self.initSC()
        
    # init methods below
    def initGUI(self):
        self.loginWindow = LoginWindow()
        self.windowStack.addWidget(self.loginWindow)
        self.statusSignal.emit(WindowStatus.LOGIN)

    def initNP(self):
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)
        self.loginWindow.numpad.loginFailure.connect(self.loginFailure)

    def initFW(self):  # sets up FileWriter!
        self.fw = FileWriter()


    def initSC(self):  # sets up SerialCommunicator!
        # set up port
        load_dotenv()
        mock = os.getenv("MOCK_SERIAL")
        if mock == "True":
            port = os.getenv("MOCK_SPORT_GS")
            self.sc = SerialCommunicator(port, 9600)
        else:
            port = os.getenv("SERIAL_PORT")
            self.sc = SerialCommunicator(port, 9600)

        # set up data signal
        self.sc.dataSignal.connect(self.dataHandler)
        self.sc.start()

    # signal update handlers below
    def dataHandler(self, data):
        # send data to each view 
        match self.status:
            case WindowStatus.INIT:
                pass
            
            case WindowStatus.LOGIN:
                pass

            case WindowStatus.RAW_TEXT:
                self.rawText.appendText(str(data))

        #FIXME need to add file writing capability, code below doesn't work
        # self.fw.addToFile(
        #     str(data)  # noqa: E128
        #     + "\n"
        # )  # noqa: E124


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
        # self.sc.start()

    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    # ui update handler
    def keyPressEvent(self, event):  # built in to pyqt5, allows us to bind keys to operations.
        if event.key() == Qt.Key_1:
            self.statusSignal.emit(WindowStatus.DEFAULT)

        elif event.key() == Qt.Key_2:
            self.statusSignal.emit(WindowStatus.LOGIN)

        elif event.key() == Qt.Key_3:
            self.statusSignal.emit(WindowStatus.RAW_TEXT)

        elif event.key() == Qt.Key_4:
            self.statusSignal.emit(Window.FC_STATUS)

        elif event.key() == Qt.Key_Escape:
            # stops the listening thread and closes the app
            if self.status == WindowStatus.RAW_TEXT:
                self.sc.stop()
                self.fw.writeEOF("outputName")

            self.close()
