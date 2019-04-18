from PyQt5 import QtCore, QtGui, QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("prac.ui")


dlg.show()
app.exec()