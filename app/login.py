from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QPalette, QColor, QPainter, QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        aiaaLogo = QLabel('cropped-aiaaweblogo-2.png')
        aiaaLogo.setPixmap(QPixmap('cropped-aiaaweblogo-2.png'))
        self.setCentralWidget(aiaaLogo)
        self.setFixedSize(QSize(800,480))

    def KeyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
