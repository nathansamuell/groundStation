from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPixmap



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()


        layout = QGridLayout()

        aiaaLogo = QLabel()
        aiaaLogo.setPixmap(QPixmap('cropped-aiaaweblogo-2.png'))
        spacerL = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding);
        spacerR = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding);
        spacerT = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding);
        spacerB = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding);

        # populate the layout
        layout.addItem(spacerT, 0,1)
        layout.addItem(spacerL,1,0)
        layout.addWidget(aiaaLogo,1,1)
        layout.addItem(spacerR,1,2)
        layout.addItem(spacerB,2,1)

        # set the layout to the window
        self.setLayout(layout)
