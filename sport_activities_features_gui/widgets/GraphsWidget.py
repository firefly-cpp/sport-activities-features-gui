from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from logic.Graphs import Graphs
class Ui_GraphsWidget(QWidget):
    exampleGraphs = [ "All biking distances ridden",
                     "Sum of biking duration for competitor",
                     "Altitude vs calories",
                     "Activity type vs calories",
                     "Map with identified hills",
                     "Map with identified intervals" ]
    graphFn = None
    
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("Form")
        self.resize(800, 600)
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 781, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.exampleGraphGroupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.exampleGraphGroupBox.setObjectName("exampleGraphGroupBox")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.exampleGraphGroupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 761, 201))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        # Add example graphs to combo box
        self.listWidget.addItems(self.exampleGraphs)
        self.listWidget.setCurrentRow(0)
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        self.btnGenerateGraph = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btnGenerateGraph.setObjectName("btnGenerateGraph")
        self.gridLayout_3.addWidget(self.btnGenerateGraph, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.exampleGraphGroupBox, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 761, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.xAxisInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.xAxisInput.setObjectName("xAxisInput")
        self.gridLayout.addWidget(self.xAxisInput, 0, 1, 1, 1)
        self.btnGenerateCustomGraph = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnGenerateCustomGraph.setObjectName("btnGenerateCustomGraph")
        self.gridLayout.addWidget(self.btnGenerateCustomGraph, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.yAxisInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yAxisInput.setObjectName("yAxisInput")
        self.gridLayout.addWidget(self.yAxisInput, 1, 1, 1, 1)
        self.btnViewAttributes = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnViewAttributes.setObjectName("btnViewAttributes")
        self.gridLayout.addWidget(self.btnViewAttributes, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        
        self.btnGenerateGraph.pressed.connect(self.generateGraph)
        self.btnGenerateCustomGraph.pressed.connect(self.generateCustomGraph)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.exampleGraphGroupBox.setTitle(_translate("Form", "Example graphs"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.btnGenerateGraph.setText(_translate("Form", "Generate graph"))
        self.groupBox.setTitle(_translate("Form", "Custom graph"))
        self.label.setText(_translate("Form", "X axis"))
        self.btnGenerateCustomGraph.setText(_translate("Form", "Generate graph"))
        self.label_2.setText(_translate("Form", "Y axis"))
        self.btnViewAttributes.setText(_translate("Form", "View data attributes"))

    def importGlobalUser(self, user):
        self.globalUser = user
        self.graphFn = Graphs(user.data)
        
    def generateGraph(self):
        chosenGraph = self.listWidget.currentItem().text()
        i = self.exampleGraphs.index(chosenGraph)
        if i != -1:
           match i:
            case 0:
                self.graphFn.allBikingDistanceRidden()
            case 1:
                self.graphFn.sumOfBikingDurationForCompetitor()
            case 2:
                self.graphFn.altitudeVsCalories()
            case 3:
                self.graphFn.activityTypeVsCalories()
            case 4:
                self.graphFn.mapWithIdentifiedHills()
            case 5:
                self.graphFn.mapWithIdentifiedIntervals()
                
    def generateCustomGraph(self):
        # Get attribute 1
        # Get attribute 2
        # Call function
        self.graphFn.customGraph()