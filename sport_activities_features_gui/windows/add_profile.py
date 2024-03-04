from PyQt6.QtWidgets import QMainWindow, QWidget, QGroupBox, QLineEdit, QPushButton, QStatusBar
from PyQt6 import QtCore


class Ui_AddProfileWindow(QMainWindow):
    _parentWindow = None

    def __init__(self, parentWindow):
        self._parentWindow = parentWindow
        QMainWindow.__init__(self)
        self.setObjectName("AddProfileWindow")
        self.resize(291, 155)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 111))
        self.groupBox.setObjectName("groupBox")
        self.profileTB = QLineEdit(self.groupBox)
        self.profileTB.setGeometry(QtCore.QRect(10, 30, 251, 22))
        self.profileTB.setObjectName("profileTB")
        self.btnAddProfile = QPushButton(self.groupBox)
        self.btnAddProfile.setGeometry(QtCore.QRect(10, 70, 251, 28))
        self.btnAddProfile.setObjectName("btnAddProfile")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.btnAddProfile.clicked.connect(self.addProfile)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddProfileWindow", "Add profile"))
        self.groupBox.setTitle(_translate(
            "AddProfileWindow", "Add new profile"))
        self.btnAddProfile.setText(_translate("AddProfileWindow", "Add"))

    def addProfile(self):
        newProfile = str(self.profileTB.text())
        self.profileTB.setText(None)
        self._parentWindow.addProfile(newProfile)
        self.close()
