import sys
from PyQt5 import QtWidgets
from windows.ProfilesWindow import Ui_ProfilesWindow

def main():   
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    profilesWindow = Ui_ProfilesWindow()
    profilesWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()