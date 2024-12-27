import shutil
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from sport_activities_features_gui.models.user import initGlobalUser, User
from sport_activities_features_gui.windows.add_profile import Ui_AddProfileWindow
from sport_activities_features_gui.windows.main_window import Ui_MainWindow
import os
from sport_activities_features_gui.global_vars import getStorePath


class Ui_ProfilesWindow(QMainWindow):
    currentProfile = None
    profileList = []

    def __init__(self):
        super().__init__()
        self.setObjectName("ProfileWindow")
        self.setWindowIcon(QtGui.QIcon('./media/Icon.png'))

        self.resize(325, 328)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 291))
        self.groupBox.setObjectName("groupBox")
        self.btnLogin = QtWidgets.QPushButton(self.groupBox)
        self.btnLogin.setGeometry(QtCore.QRect(20, 250, 251, 28))
        self.btnLogin.setObjectName("btnLogin")
        self.btnAddProfile = QtWidgets.QPushButton(self.groupBox)
        self.btnAddProfile.setGeometry(QtCore.QRect(20, 220, 121, 28))
        self.btnAddProfile.setObjectName("btnAddProfile")
        self.btnRemoveProfile = QtWidgets.QPushButton(self.groupBox)
        self.btnRemoveProfile.setGeometry(QtCore.QRect(150, 220, 121, 28))
        self.btnRemoveProfile.setObjectName("btnRemoveProfile")
        self.profilesLV = QtWidgets.QListWidget(self.groupBox)
        self.profilesLV.setGeometry(QtCore.QRect(20, 30, 256, 185))

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.profilesLV.itemClicked.connect(self.profileSelected)
        self.btnLogin.clicked.connect(self.login)
        self.btnAddProfile.clicked.connect(self.showAddProfileWindow)
        self.btnRemoveProfile.clicked.connect(self.removeProfile)

        self.addProfileWindow = Ui_AddProfileWindow(self)
        storePath = getStorePath()
        if not os.path.exists(storePath):
            os.mkdir(storePath)
        with os.scandir(storePath) as entries:
            for entry in entries:
                self.profileList.append(entry.name)

        # Add profiles to list view
        for profile in self.profileList:
            self.profilesLV.addItem(profile)
        # Set initial chosen profile
        if len(self.profileList) > 0:
            self.profilesLV.setCurrentRow(0)
            self.currentProfile = self.profileList[0]

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle("Profiles")
        self.groupBox.setTitle("Profiles")
        self.btnLogin.setText("Log in")
        self.btnAddProfile.setText("Add profile")
        self.btnRemoveProfile.setText("Remove profile")
        __sortingEnabled = self.profilesLV.isSortingEnabled()
        self.profilesLV.setSortingEnabled(False)
        self.profilesLV.setSortingEnabled(__sortingEnabled)

    # SELECT PROFILE
    def profileSelected(self):
        self.currentProfile = str(self.profilesLV.currentItem().text()).lower()

    # LOGIN
    def login(self):
        if self.currentProfile is not None:
            self.hide()
            user: User = initGlobalUser(self.currentProfile, [])
            self.dialog = Ui_MainWindow()
            self.dialog.importGlobalUser(user)
            self.dialog.show()
        else:
            QMessageBox.warning(
                self, 'Warning', 'Add a profile first', QMessageBox.StandardButton.Ok)

    # ADD PROFILE
    def showAddProfileWindow(self):
        self.addProfileWindow.show()

    def addProfile(self, newProfile: str):
        if newProfile in self.profileList:
            QMessageBox.warning(
                self, 'Warning', 'The profile you entered already exists', QMessageBox.StandardButton.Ok)
            return

        newProfileItem = QtWidgets.QListWidgetItem(newProfile)
        newProfileItem.setText(newProfile)
        self.profilesLV.addItem(newProfileItem)
        self.profileList.append(newProfile)
        self.profilesLV.setCurrentRow(len(self.profileList) - 1)
        self.currentProfile = newProfile

        newProfilePath = os.path.join(getStorePath(), newProfile)
        if not os.path.isdir(newProfilePath):
            os.makedirs(newProfilePath)

    # REMOVE PROFILE
    def removeProfile(self):
        reply = QMessageBox.question(self, 'Message',
                                     f"Do you really want to delete the profile \"{str(self.currentProfile)}\"",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:            
            deletePath = os.path.join(getStorePath(), self.currentProfile)
            try:
                listItems = self.profilesLV.selectedItems()
                if not listItems:
                    return
                shutil.rmtree(deletePath)
                for item in listItems:
                    self.profilesLV.takeItem(self.profilesLV.row(item))
                self.profileList.remove(self.currentProfile)
                self.currentProfile = None
            except OSError as e:
                print("Error: %s : %s" % (deletePath, e.strerror))
