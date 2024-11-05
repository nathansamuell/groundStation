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

from dotenv import load_dotenv
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QSpacerItem, QWidget


class Numpad(QWidget):

    # authenticator signals
    loginSuccess = pyqtSignal()
    loginFailure = pyqtSignal()

    def __init__(self):
        super().__init__()

        load_dotenv()
        layout = QGridLayout()
        self.loginPin = ""
        # create button list
        buttons = []
        enterButton = QPushButton("ENTER")  # a special button
        # create button size policy
        buttonPolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        enterButton.setSizePolicy(buttonPolicy)
        # create buttons
        for i in list(range(1, 10)) + [0]:
            button = QPushButton(str(i))
            button.setSizePolicy(buttonPolicy)
            button.clicked.connect(
                lambda checked, button=button: self.buttonClicked(button)
            )
            buttons.append(button)

        buttons.append(enterButton)
        enterButton.clicked.connect(lambda: self.buttonClicked(enterButton))

        lSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Ignored)
        # rSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Ignored)

        # add buttons to layout
        layout.addWidget(buttons[0], 0, 0)
        layout.addWidget(buttons[1], 0, 1)
        layout.addWidget(buttons[2], 0, 2)
        layout.addWidget(buttons[3], 1, 0)
        layout.addWidget(buttons[4], 1, 1)
        layout.addWidget(buttons[5], 1, 2)
        layout.addWidget(buttons[6], 2, 0)
        layout.addWidget(buttons[7], 2, 1)
        layout.addWidget(buttons[8], 2, 2)
        layout.addItem(lSpacer, 3, 0)
        layout.addWidget(buttons[9], 3, 1)
        layout.addWidget(buttons[10], 3, 2)

        # set the layout to the window
        self.setLayout(layout)

    def buttonClicked(self, buttonClicked):
        if buttonClicked.text() == "1":
            self.loginPin = self.loginPin + "1"

        elif buttonClicked.text() == "2":
            self.loginPin = self.loginPin + "2"

        elif buttonClicked.text() == "3":
            self.loginPin = self.loginPin + "3"

        elif buttonClicked.text() == "4":
            self.loginPin = self.loginPin + "4"

        elif buttonClicked.text() == "5":
            self.loginPin = self.loginPin + "5"

        elif buttonClicked.text() == "6":
            self.loginPin = self.loginPin + "6"

        elif buttonClicked.text() == "7":
            self.loginPin = self.loginPin + "7"

        elif buttonClicked.text() == "8":
            self.loginPin = self.loginPin + "8"

        elif buttonClicked.text() == "9":
            self.loginPin = self.loginPin + "9"

        elif buttonClicked.text() == "0":
            self.loginPin = self.loginPin + "0"
        else:

            # print("enter button pressed")
            # print(self.loginPin)
            self.authenticate()

    def authenticate(self):
        enteredPassword = self.loginPin
        userPin = os.getenv("USER_PIN")
        # print(userPin)
        # print("authenticate method called")

        if userPin == enteredPassword:
            self.loginSuccess.emit()
            # print("login signal emit call reached")
        else:
            self.loginFailure.emit()
            # print("login failure emit call reached")
        self.loginPin = ""
