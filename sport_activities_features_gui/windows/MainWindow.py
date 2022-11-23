from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from logic import ImportData

from widgets.ImportData import Ui_ImportData

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("Sport Activities Features GUI")
        self.setEnabled(True)
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.btn_ImportData = QtWidgets.QMenu(self.menubar)
        self.btn_ImportData.setObjectName("btn_ImportData")
        self.btn_Graphs = QtWidgets.QMenu(self.menubar)
        self.btn_Graphs.setObjectName("btn_Graphs")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_Data = QtWidgets.QAction(self)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionCalender = QtWidgets.QAction(self)
        self.actionCalender.setObjectName("actionCalender")
        self.actionGraphs = QtWidgets.QAction(self)
        self.actionGraphs.setObjectName("actionGraphs")
        self.actionTransformations = QtWidgets.QAction(self)
        self.actionTransformations.setObjectName("actionTransformations")
        self.menuFile.addAction(self.actionExit)
        self.btn_ImportData.addAction(self.actionImport_Data)
        self.btn_ImportData.addSeparator()
        self.btn_ImportData.addAction(self.actionCalender)
        self.btn_ImportData.addSeparator()
        self.btn_ImportData.addAction(self.actionTransformations)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.btn_ImportData.menuAction())
        self.menubar.addAction(self.btn_Graphs.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
        #self.mainStackedWidget.addWidget(Ui_ImportData())
        #self.mainStackedWidget.setCurrentIndex(-1)
        
        self.actionExit.triggered.connect(self.close)
        
        #self.actionImport_Data.triggered.connect(lambda : self.mainStackedWidget.setCurrentIndex(1))
        
        # ADDING WIDGETS TO MAIN STACKED WIDGET
        self.mainStackedWidget.addWidget(Ui_ImportData())
        
        # TRIGGERING WIDGETS
        self.actionImport_Data.triggered.connect(lambda : self.mainStackedWidget.setCurrentIndex(1))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.btn_ImportData.setTitle(_translate("MainWindow", "Options"))
        self.btn_Graphs.setTitle(_translate("MainWindow", "Graphs"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionCalender.setText(_translate("MainWindow", "Calender"))
        self.actionGraphs.setText(_translate("MainWindow", "Graphs"))
        self.actionTransformations.setText(_translate("MainWindow", "Transformations"))
