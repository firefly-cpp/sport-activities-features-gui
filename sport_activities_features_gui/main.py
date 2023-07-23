import sys
from PyQt6 import QtWidgets
from sport_activities_features_gui.windows.profiles_window import Ui_ProfilesWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    profilesWindow = Ui_ProfilesWindow()
    profilesWindow.show()
    sys.exit(app.exec())

def icon_loader_for_win32(): # Windows needs this to display the icon in the taskbar
    if sys.platform == "win32":
        import ctypes
        myappid = 'firefly-cpp.sport-activities-features.gui'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



if __name__ == '__main__':
    icon_loader_for_win32()
    main()
