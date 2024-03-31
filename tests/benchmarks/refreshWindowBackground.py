import random
import sys

from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.iterations = 0
        self.currentColor = QColor(255, 255, 255)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # self.refreshWindowTitle = False
        self.button = QPushButton("Start Refresh Test")
        # self.setWindowTitle("Background Refresh Test")
        self.button.clicked.connect(self.startTest)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.setCentralWidget(self.button)
        self.button.setFixedSize(200, 50)
        self.setFixedSize(QSize(800, 480))

    def startTest(self):
        self.timer.start(50)
        self.iterations = 0

    def refresh(self):
        if self.iterations < 100:
            self.currentColor = QColor(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
            self.update()
            self.iterations += 1

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.fillRect(self.rect(), self.currentColor)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            print("Escape key pressed. Closing application.")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
