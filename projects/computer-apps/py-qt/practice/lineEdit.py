from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton, QLineEdit, QWidget
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Line Edit"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowIcon(QtGui.QIcon("image/prosenjit.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 13))
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.lineedit)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 13))
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())