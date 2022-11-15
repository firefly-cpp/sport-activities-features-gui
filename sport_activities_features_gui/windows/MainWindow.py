from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp
from logic import quit, setImportData

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.btn_ImportData = QtWidgets.QMenu(self.menubar)
        self.btn_ImportData.setObjectName("btn_ImportData")
        self.btn_Calender = QtWidgets.QMenu(self.menubar)
        self.btn_Calender.setObjectName("btn_Calender")
        self.btn_Graphs = QtWidgets.QMenu(self.menubar)
        self.btn_Graphs.setObjectName("btn_Graphs")
        self.btn_Transformations = QtWidgets.QMenu(self.menubar)
        self.btn_Transformations.setObjectName("btn_Transformations")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.btn_ImportData.menuAction())
        self.menubar.addAction(self.btn_Calender.menuAction())
        self.menubar.addAction(self.btn_Graphs.menuAction())
        self.menubar.addAction(self.btn_Transformations.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionExit.triggered.connect(self.appQuit)
        self.btn_ImportData.triggered.connect(self.importData)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle('Sports activities features GUI')
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.btn_ImportData.setTitle(_translate("MainWindow", "Import Data"))
        self.btn_Calender.setTitle(_translate("MainWindow", "Calender"))
        self.btn_Graphs.setTitle(_translate("MainWindow", "Graphs"))
        self.btn_Transformations.setTitle(_translate("MainWindow", "Transformations"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    def importData(self):
        setImportData()
    
    def appQuit(self):
        quit()