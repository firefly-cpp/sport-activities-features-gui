import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction
from PyQt5.QtCore import QSize
from functions import MultiThread
from sport_activities_features_gui.windows.ProfilesWindow import Ui_ProfilesWindow
from windows.MainWindow import Ui_MainWindow
from models.User import User

def main():
    
    User()
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    profilesWindow = Ui_ProfilesWindow()
    profilesWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()