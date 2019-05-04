from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Events and Signals"
        left = 500
        top = 200
        width = 300
        height = 250
        icon = 'image/prosenjit.png'

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setGeometry(left, top, width, height)

        # Button
        self.CreateButton()

        self.show()

    def CreateButton(self):
        button = QPushButton("Close Application", self)
        # button.move(50, 50)
        button.setGeometry(QRect(100, 100, 150, 50))
        button.setIcon(QtGui.QIcon("image/download.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

