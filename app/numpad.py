# imports
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QPushButton

class Numpad(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        # create button list
        buttons = []
        enterButton = QPushButton("ENTER") # a special button
        # create button size policy
        buttonPolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        enterButton.setSizePolicy(buttonPolicy)
        # create buttons
        for i in list(range(1,10))+[0]:
            button = QPushButton(str(i))
            button.setSizePolicy(buttonPolicy)
            buttons.append(button)
        buttons.append(enterButton)

        lSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Ignored)
        rSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Ignored)

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
