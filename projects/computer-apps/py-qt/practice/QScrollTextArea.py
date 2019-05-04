# from PyQt5.QtWidgets import QApplication, QPushButton, QDialog,\
#     QGroupBox, QGridLayout, QVBoxLayout, QLabel, QMainWindow,\
#     QHBoxLayout, QRadioButton, QLineEdit, QWidget, QButtonGroup,\
#     QSizeGrip, QFrame, QSplitter, QSlider, QFormLayout, QScrollArea
# import sys
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtCore import QRect, Qt
# from PyQt5.QtGui import QPixmap
#
#
# class Window(QWidget):
#     def __init__(self, val):
#         super().__init__()
#
#         self.title = "PyQt5 Scroll Area"
#         self.left = 500
#         self.top = 200
#         self.width = 300
#         self.height = 250
#
#         self.setWindowIcon(QtGui.QIcon("image/prosenjit.ico"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.setStyleSheet('background-color:green')
#
#         # -------- ------------ ---------
#         formLayout = QFormLayout()
#         groupbox = QGroupBox("This is Group Box")
#
#         labelList = []
#         buttonList = []
#
#         for i in range(val):
#             labelList.append(QLabel("Label"))
#             labelList.append(QPushButton("Click Me"))
#             formLayout.addRow(labelList[i], buttonList[i])
#
#         groupbox.setLayout(formLayout)
#         scroll = QScrollArea()
#         scroll.setWidget(groupbox)
#         scroll.setWidgetResizable(True)
#         scroll.setFixedHeight(400)
#
#         layout = QVBoxLayout()
#         layout.addWidget(scroll)
#
#         self.setLayout(layout)
#
#         self.show()
#
#
# if __name__ == "__main__":
#     App = QApplication(sys.argv)
#     window = Window(10)
#     sys.exit(App.exec())

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys


class Window(QWidget):
    def __init__(self, val):
        super().__init__()

        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout =QFormLayout()

        groupBox = QGroupBox("This Is Group Box")

        labelLis = []
        comboList = []

        for i in  range(val):
            labelLis.append(QLabel("Label"))
            comboList.append(QPushButton("Click Me"))
            formLayout.addRow(labelLis[i], comboList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

        self.show()


App = QApplication(sys.argv)
window = Window(30)
sys.exit(App.exec())