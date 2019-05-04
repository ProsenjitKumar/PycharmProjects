from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton, QLineEdit, QWidget, QButtonGroup,\
    QSizeGrip, QFrame

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Size Group"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowIcon(QtGui.QIcon("image/prosenjit.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:green')

        # -------- ------------ ---------
        hbox = QHBoxLayout()

        btn = QPushButton("Click me")
        btn.setStyleSheet("color:white")
        btn.setStyleSheet("background-color:red")

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet('background-color:red')
        frame.setLineWidth(0.1)

        hbox.addWidget(frame)
        hbox.addWidget(btn)

        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())