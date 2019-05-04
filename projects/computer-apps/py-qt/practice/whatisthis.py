from PyQt5.QtWidgets import QApplication, QPushButton, QLabel,\
    QHBoxLayout, QWidget
import sys
from PyQt5 import QtGui

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "What is this class"
        self.left = 200
        self.top = 400
        self.width = 400
        self.height = 400
        self.icon = 'image/prosenjit.png'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and Press SHIFT + F1")
        hbox.addWidget(label)

        button = QPushButton("Click Me", self)
        button.setWhatsThis("This is a button you can click")
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())