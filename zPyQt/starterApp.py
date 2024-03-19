# copied from https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/


# imports
from PyQt5.QtWidgets import QApplication, QWidget # basic PyQT imports
import sys # used for command line arguments (yes please!)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
# above copied direct from website about line 15^^


# here's our ONE QApp instance -- see above for no CLI arguments^
app = QApplication(sys.argv)

window = QWidget() # windows in PyQT are widgets!
window.show() # MUST be specified -- windows are shown by default

app.exec() # starts your execution loop

# Code down here isn't accessed until you exit.