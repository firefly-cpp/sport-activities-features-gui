import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction
from PyQt5.QtCore import QSize
from functions import MultiThread

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(1024, 768))
        self.setWindowTitle('Sports activities features gui')


def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()