import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction
from PyQt5.QtCore import QSize
from functions import MultiThread

from windows.MainWindow import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    mainWindow = Ui_MainWindow()
        
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()