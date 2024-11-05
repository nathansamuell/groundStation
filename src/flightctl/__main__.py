# SRAD Avionics Ground Software for AIAA UH
#
# Copyright (c) 2024 Nathan Samuell (www.github.com/nathansamuell)
# Licensed under the MIT License
#
# More information on the MIT license as well as a complete copy
# of the license can be found here: https://choosealicense.com/licenses/mit/
# All above text must be included in any restribution.

# imports
import sys

from flightctl.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # start app
    app = QApplication(sys.argv)
    window = MainWindow()
    window.initGUI()
    window.show()
    app.exec()
