# qt imports
from PyQt5.QtCore import QSize, Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPixmap, QFont

# app class imports
from numpad import Numpad


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()


        aiaaLogo = QLabel()
        aiaaLogo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding))
        self.enterPinText = QLabel("       Enter PIN:")
        self.enterPinText.setFixedHeight(150)
        font = QFont()
        font.setPointSize(16)
        self.enterPinText.setFont(font)

        spacerL = QSpacerItem(240,QSizePolicy.Ignored)
        spacerR = QSpacerItem(240,QSizePolicy.Ignored)
        

        aiaaLogo.setPixmap(QPixmap('cropped-aiaaweblogo-2.png'))
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
