from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget, QMessageBox

class Ui_GraphsWidget(QWidget):
    exampleGraphs = ["All biking distances ridden",
                     "Sum of biking duration for competitor",
                     "Altitude vs calories",
                     "Calories by activity type",
                     "Heart rate by activities"]
    graphFn = None
    refMainWindow = None

    def __init__(self, refMainWindow):
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
        self.exampleGraphGroupBox = QtWidgets.QGroupBox(
            self.gridLayoutWidget_2)
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 761, 171))
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
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.yAxisInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.yAxisInput.setObjectName("yAxisInput")
        self.gridLayout.addWidget(self.yAxisInput, 1, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plotTypeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.plotTypeComboBox.setObjectName("comboBox")
        self.plotTypeComboBox.addItem("Bar")
        self.plotTypeComboBox.addItem("Scatter")
        self.plotTypeComboBox.addItem("Line")
        self.gridLayout_4.addWidget(self.plotTypeComboBox, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnGenerateCustomGraph = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.btnGenerateCustomGraph.setObjectName("btnGenerateCustomGraph")
        self.gridLayout.addWidget(self.btnGenerateCustomGraph, 2, 2, 1, 1)

        self.btnViewAttributesX = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnViewAttributesX.setObjectName("btnViewAttributesX")
        self.gridLayout.addWidget(self.btnViewAttributesX, 0, 2, 1, 1)

        self.btnViewAttributesY = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnViewAttributesY.setObjectName("btnViewAttributesY")
        self.gridLayout.addWidget(self.btnViewAttributesY, 1, 2, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.viewAttributesWindow = Ui_ViewAttributesWindow()
        self.viewAttributesWindow.callback = self.setSelectedAtribute

        self.plotTypeComboBox.setCurrentText("Bar")
        self.xAxisInput.setEnabled(False)
        self.btnViewAttributesX.setEnabled(False)
        self.yAxisInput.setEnabled(True)
        self.plotTypeComboBox.currentTextChanged.connect(
            self.on_combobox_changed)
        self.btnGenerateGraph.pressed.connect(self.generateGraph)
        self.btnGenerateCustomGraph.pressed.connect(self.generateCustomGraph)
        self.btnViewAttributesX.pressed.connect(
            lambda: self.viewAttributes("X"))
        self.btnViewAttributesY.pressed.connect(
            lambda: self.viewAttributes("Y"))

        self.retranslateUi()
        self.refMainWindow = refMainWindow

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.exampleGraphGroupBox.setTitle(
            _translate("Form", "Example graphs"))
        self.btnGenerateGraph.setText(_translate("Form", "Generate graph"))
        self.groupBox.setTitle(_translate("Form", "Custom graph"))
        self.label.setText(_translate("Form", "X axis"))
        self.btnGenerateCustomGraph.setText(
            _translate("Form", "Generate graph"))
        self.label_2.setText(_translate("Form", "Y axis"))
        self.btnViewAttributesX.setText(
            _translate("Form", "View data attributes for X"))
        self.btnViewAttributesY.setText(
            _translate("Form", "View data attributes for Y"))

    def importGlobalUser(self, user):
        self.globalUser = user
        self.graphFn = Graphs(user)
        self.viewAttributesWindow.importData(user.data)

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
                    self.graphFn.caloriesByActivityType()
                case 4:
                    self.graphFn.heartRateByActivities()

    def generateCustomGraph(self):
        xAttr = self.xAxisInput.text()
        yAttr = self.yAxisInput.text()
        plotType = self.plotTypeComboBox.currentText()
        try:
            self.graphFn.customGraph(xAttr, yAttr, plotType)
        except Exception as e:
            if type(e) == KeyError:
                QMessageBox.warning(
                    self, 'Warning', f"Please enter valid attributes. {str(e)} is not a valid attribute.")
            else:
                QMessageBox.warning(self, 'Warning', str(e))

    def viewAttributes(self, axis):
        self.viewAttributesWindow.axis = axis
        self.viewAttributesWindow.show()

    def setSelectedAtribute(self):
        if self.viewAttributesWindow.result:
            if self.viewAttributesWindow.axis == "X":
                self.xAxisInput.setText(
                    self.viewAttributesWindow.selectedAttribute)
            else:
                self.yAxisInput.setText(
                    self.viewAttributesWindow.selectedAttribute)

    def on_combobox_changed(self, value):
        if (value == "Bar" or value == "Line"):
            self.xAxisInput.setEnabled(False)
            self.btnViewAttributesX.setEnabled(False)
        else:
            self.xAxisInput.setEnabled(True)
            self.btnViewAttributesX.setEnabled(True)


from sport_activities_features_gui.windows.view_attributes_window import Ui_ViewAttributesWindow
from sport_activities_features_gui.logic.graphs import Graphs