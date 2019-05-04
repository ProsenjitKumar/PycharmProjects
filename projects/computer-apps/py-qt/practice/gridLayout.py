from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Grid Layout Management"
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
        self.groupBox = QGroupBox("What Is Your Favourite Programming Language?")
        gridLayout = QGridLayout()

        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon("image/download.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0, 0)

        button3 = QPushButton("C", self)
        button3.setIcon(QtGui.QIcon("image/t5.jpg"))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 0, 1)

        button1 = QPushButton("C++", self)
        button1.setIcon(QtGui.QIcon("image/download.png"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 1, 0)

        button2 = QPushButton("Java", self)
        button2.setIcon(QtGui.QIcon("image/t2.jpg"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())