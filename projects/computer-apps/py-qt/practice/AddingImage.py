from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Image Adding"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 300
        self.icon = 'image/prosenjit.png'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("image/pro.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())