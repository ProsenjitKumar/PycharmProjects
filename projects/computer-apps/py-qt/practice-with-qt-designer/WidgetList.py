from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication([])
dlg = uic.loadUi("widgetlist.ui")


def addItem():
    if not dlg.lineEdit.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit.text())
        dlg.lineEdit.setText("")


def show_message(title, message):
    QMessageBox.information(None, title, message)


show_message("Warning!", "Automeated open")


dlg.pushButton.clicked.connect(addItem)
dlg.lineEdit.returnPressed.connect(addItem)


if __name__ == "__main__":
    dlg.show()
    app.exec()