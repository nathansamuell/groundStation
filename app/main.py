# QT Imports
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPixmap
import sys

# Local Imports
from login import LoginWindow
from numpad import Numpad

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        fillerButton = QPushButton("filler button")
        self.windowStack = QStackedLayout()
        self.loginWindow = LoginWindow()
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)

        button = QPushButton("filler button")
        self.windowStack.addWidget(self.loginWindow)
        self.windowStack.addWidget(fillerButton)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800,480)
        self.showFullScreen()

    def loginSuccess(self):
        self.windowStack.setCurrentIndex(1)

    def loginFailure(self):
        self.loginWindow.enterPinText = "IncorrectPin--try again:"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_1:
            self.windowStack.setCurrentIndex(0)
        if event.key() == Qt.Key_2:
            self.windowStack.setCurrentIndex(1)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
