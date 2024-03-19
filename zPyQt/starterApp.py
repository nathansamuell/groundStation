# copied from https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/


# imports
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton # basic PyQT imports
import sys # used for command line arguments (yes please!)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
# above copied direct from website about line 15^^



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App") # window title method
        button = QPushButton("Press Me!") # default button variable modified

        self.setFixedSize(QSize(400,300)) # locks the window size. no more resizing!

        # sets the central widget of the window to the button
        self.setCentralWidget(button)



# here's our ONE QApp instance -- see above for no CLI arguments^
app = QApplication(sys.argv)

window = MainWindow() # windows in PyQT are widgets!
window.show() # MUST be specified -- windows are shown by default

app.exec() # starts your execution loop

# Code down here isn't accessed until you exit.