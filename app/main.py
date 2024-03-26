# QT Imports
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPixmap
import sys

# Local Imports
from login import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowStack = QStackedLayout()
        loginWindow = LoginWindow()
        button = QPushButton("filler button")
        self.windowStack.addWidget(loginWindow)
        self.windowStack.addWidget(button)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.showFullScreen()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
