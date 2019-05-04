from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
    QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
    QHBoxLayout, QRadioButton, QCalendarWidget
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
        self.height = 450
        self.icon = 'image/prosenjit.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.calendar()

        self.show()

    def calendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.onSelectionChanged)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet("color:green")

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def onSelectionChanged(self):
        ca = self.calendar.selectedDate()
        self.label.setText(str(ca))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())