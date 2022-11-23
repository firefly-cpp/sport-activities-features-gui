from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from windows.MainWindow import Ui_MainWindow
import sys

class Ui_ProfilesWindow(QMainWindow):
    currentProfile = 'anoymous'
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("ProfileWindow")
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
        self.profilesLV.setGeometry(QtCore.QRect(20, 20, 256, 192))
        self.profilesLV.setObjectName("profilesLV")
        item = QtWidgets.QListWidgetItem()
        self.profilesLV.addItem(item)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.profilesLV.itemActivated.connect(self.profileSelected)
        self.btnLogin.clicked.connect(self.login)
        self.dialog = Ui_MainWindow()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def profileSelected(profile):
        print(profile.text())
        global currentProfile 
        currentProfile = profile.text()
    
    def login(self):
        self.hide()
        self.dialog.show()
        
    def addProfile():
        print("Not implemented")
        
    def removeProfile():
        print("Not implemented")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Profiles"))
        self.btnLogin.setText(_translate("MainWindow", "Log in"))
        self.btnAddProfile.setText(_translate("MainWindow", "Add profile"))
        self.btnRemoveProfile.setText(_translate("MainWindow", "Remove profile"))
        __sortingEnabled = self.profilesLV.isSortingEnabled()
        self.profilesLV.setSortingEnabled(False)
        item = self.profilesLV.item(0)
        item.setText(_translate("MainWindow", "Anonymous"))
        self.profilesLV.setSortingEnabled(__sortingEnabled)
