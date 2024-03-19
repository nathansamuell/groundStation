# copied from https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.button_is_checked = True #default for this value is false

        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me")
        self.button.setCheckable(False)
        self.button.clicked.connect(self.the_button_was_clicked) # .clicked method is a signal! .connect is where it sends the signal
        #self.button.clicked.connect(self.the_button_was_toggled) # this new function includes an argument the toggled state from the clicked signal. 
                                                            # Signals can also send data!

        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv);

window = MainWindow()
window.show()

app.exec()