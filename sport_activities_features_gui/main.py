import sys
from PyQt5 import QtWidgets
from windows.MainWindow import Ui_MainWindow
from config import app, ui_mainWindow, ui_importData

class Main:
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui_mainWindow = Ui_MainWindow()
        ui_mainWindow.setupUi(MainWindow) 
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main = Main()
    main.run()
    