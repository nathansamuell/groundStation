# imports
import sys
from random import choice

from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window_titles = {i: f"Window Title {i}" for i in range(1, 101)}
        self.iterations = 0

        # self.refreshWindowTitle = False
        self.button = QPushButton("Start Refresh Test")
        self.button.clicked.connect(self.startTest)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.setCentralWidget(self.button)
        self.setFixedSize(QSize(800, 480))
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def startTest(self):
        self.iterations = 0
        self.timer.start(50)
        # print("Changed window title!");

    def refresh(self):
        if self.iterations < 100:
            new_window_title = choice(list(self.window_titles.values()))
            self.setWindowTitle(new_window_title)
            self.iterations += 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            print("Escape key pressed. Closing application.")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
