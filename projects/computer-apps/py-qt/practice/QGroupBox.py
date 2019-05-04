from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton, QLineEdit, QWidget, QButtonGroup

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Group Box"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowIcon(QtGui.QIcon("image/prosenjit.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # -------- ------------ ---------

        hbox = QHBoxLayout()

        groupbox = QGroupBox("Select your favourite Fruit.")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(groupbox)

        vbox = QVBoxLayout()
        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Melon")
        vbox.addWidget(rad3)

        groupbox.setLayout(vbox)
        self.setLayout(hbox)

        self.show()

    def on_click_button(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + " Was clicked ")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())