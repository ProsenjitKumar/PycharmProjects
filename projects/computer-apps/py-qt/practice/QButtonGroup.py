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

        self.title = "Button Group"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowIcon(QtGui.QIcon("image/prosenjit.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 14))
        hbox.addWidget(self.label)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_click_button)

        button = QPushButton("Python")
        button.setIcon(QtGui.QIcon("image/download.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setFont(QtGui.QFont("Sanserif", 14))
        self.buttongroup.addButton(button, 0)
        hbox.addWidget(button)

        button1 = QPushButton("C")
        button1.setIcon(QtGui.QIcon("image/download.png"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setFont(QtGui.QFont("Sanserif", 14))
        self.buttongroup.addButton(button1, 1)
        hbox.addWidget(button1)

        button2 = QPushButton("Java")
        button2.setIcon(QtGui.QIcon("image/download.png"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setFont(QtGui.QFont("Sanserif", 14))
        self.buttongroup.addButton(button2, 2)
        hbox.addWidget(button2)

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