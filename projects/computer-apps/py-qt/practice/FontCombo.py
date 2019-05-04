from PyQt5 import QtGui, QtCore
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    main_layout = QtGui.QVBoxLayout()
    # QComboBox
    combo = QtGui.QComboBox()
    model = combo.model()
    for row in range(10):
        item = QtGui.QStandardItem(str(row))
        item.setForeground(QtGui.QColor('red'))
        font = item.font()
        font.setPointSize(10)
        item.setFont(font)
        model.appendRow(item)
    main_layout.addWidget(combo)

    ok_button = QtGui.QPushButton("OK")
    ok_button.clicked.connect(OK)
    main_layout.addWidget(ok_button)

    main_layout.addStretch(1)
    window.setLayout(main_layout)
    window.show()
    sys.exit(app.exec_())

def OK(self):
    print('OK')

if __name__ == '__main__':
    main()