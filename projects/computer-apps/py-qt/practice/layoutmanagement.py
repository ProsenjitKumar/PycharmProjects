from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.icon = 'image/prosenjit.png'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favourite Spot?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon("image/download.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Cricket", self)
        button1.setIcon(QtGui.QIcon("image/t1.jpg"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Tennis", self)
        button2.setIcon(QtGui.QIcon("image/t2.jpg"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())