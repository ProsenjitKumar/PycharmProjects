from PyQt5 import QtWidgets, uic


def converter():
    dlg.lineEditConverter2.setText(str(float(dlg.lineEditConverter1.text()) / 80))


app = QtWidgets.QApplication([])
dlg = uic.loadUi("converter.ui")

dlg.lineEditConverter1.setFocus()
dlg.lineEditConverter1.returnPressed.connect(converter)
dlg.pushButtonConvert.clicked.connect(converter)


if __name__ == "__main__":
    dlg.show()
    app.exec()