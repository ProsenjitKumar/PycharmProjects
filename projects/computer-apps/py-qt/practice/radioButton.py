from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Radio Button"
        self.left = 300
        self.top = 400
        self.width = 400
        self.height = 100
        self.icon = 'image/prosenjit.png'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("What Is Your Favourite Spot?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 10))

        hboxlayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("Python")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon("image/download.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 14))
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("C")
        self.radiobtn2.setIcon(QtGui.QIcon("image/download.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 14))
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("C++")
        self.radiobtn3.setIcon(QtGui.QIcon("image/download.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 14))
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn3)

        self.radiobtn4 = QRadioButton("Java")
        self.radiobtn4.setIcon(QtGui.QIcon("image/download.png"))
        self.radiobtn4.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn4.setFont(QtGui.QFont("Sanserif", 14))
        self.radiobtn4.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn4)

        self.groupBox.setLayout(hboxlayout)

    def onRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You gave selected " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())