import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction
from PyQt5.QtCore import QSize
from functions import MultiThread

from windows.MainWindow import Ui_MainWindow

import logic
from config import app, ui_mainWindow, ui_importData

def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui_mainWindow = Ui_MainWindow()
    ui_mainWindow.setupUi(MainWindow)
        
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()