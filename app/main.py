# imports
import sys

from login import LoginWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        fillerButton = QPushButton("filler button")
        self.windowStack = QStackedLayout()
        self.loginWindow = LoginWindow()
        self.loginWindow.numpad.loginSuccess.connect(self.loginSuccess)
        self.loginWindow.numpad.loginFailure.connect(self.loginFailure)

        self.windowStack.addWidget(self.loginWindow)
        self.windowStack.addWidget(fillerButton)

        mainWidget = QWidget()
        mainWidget.setLayout(self.windowStack)
        self.setCentralWidget(mainWidget)
        self.setFixedSize(800, 480)
        self.showFullScreen()

    def loginSuccess(self):
        self.windowStack.setCurrentIndex(1)

    def loginFailure(self):
        self.loginWindow.enterPinText.setText("Incorrect Pin--Try Again: ")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_1:
            self.windowStack.setCurrentIndex(0)
        if event.key() == Qt.Key_2:
            self.windowStack.setCurrentIndex(1)


# start app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
