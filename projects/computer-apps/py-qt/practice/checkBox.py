from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton, QCheckBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Check Box"
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

        self.checkBox()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def checkBox(self):
        self.groupBox = QGroupBox("What Is Your Favourite Spot?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 10))

        hboxlayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("image/download.png"))
        self.check1.setIconSize(QtCore.QSize(40, 40))
        self.check1.setFont(QtGui.QFont("Sanserif", 14))
        self.check1.toggled.connect(self.onCheckBtn)
        hboxlayout.addWidget(self.check1)

        self.check2 = QCheckBox("C")
        self.check2.setIcon(QtGui.QIcon("image/download.png"))
        self.check2.setIconSize(QtCore.QSize(40, 40))
        self.check2.setFont(QtGui.QFont("Sanserif", 14))
        self.check2.toggled.connect(self.onCheckBtn)
        hboxlayout.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setIcon(QtGui.QIcon("image/download.png"))
        self.check3.setIconSize(QtCore.QSize(40, 40))
        self.check3.setFont(QtGui.QFont("Sanserif", 14))
        self.check3.toggled.connect(self.onCheckBtn)
        hboxlayout.addWidget(self.check3)

        self.groupBox.setLayout(hboxlayout)

    def onCheckBtn(self):
        if self.check1.isChecked():
            self.label.setText("You have selected " + self.check1.text())

        if self.check2.isChecked():
            self.labe1.setText("You have selected " + self.check2.text())

        if self.check3.isChecked():
            self.labe1.setText("You have selected " + self.check3.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())