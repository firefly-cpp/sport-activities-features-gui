from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from PyQt6.QtGui import QAction
from logic.ImportData import ImportData
from logic.Transformations import Transformations
from models.User import User
import pandas as pd

class Ui_TransformationsWidget(QWidget):
    globalUser: User
    importDataFn: ImportData
    transformations: Transformations
    
    def __init__(self):
        QWidget.__init__(self)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.setObjectName("Transformations")
        self.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 370, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(10, 430, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tableWidget = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        



    def retranslateUi(self, Transformations):
        _translate = QtCore.QCoreApplication.translate
        Transformations.setWindowTitle(_translate("Transformations", "Frame"))
        self.pushButton.setText(_translate("Transformations", "Min-Max"))
        self.pushButton_2.setText(_translate("Transformations", "Log"))
        self.pushButton_3.setText(_translate("Transformations", "Z-Score"))
        self.checkBox.setText(_translate("Transformations", "One hot encoding"))
    

    def importGlobalUser(self, user: User):
        self.globalUser = user
        self.importDataFn = ImportData(user)
        if(self.globalUser.data.empty is False):
            self.OutPutExistingData(self.globalUser.data)

    def OutPutExistingData(self, dataframe : pd.DataFrame):
        df2 = dataframe.copy()
        df2 = df2.drop(columns=['positions', 'altitudes', 'distances', 'timestamps', 'speeds','heartrates'])

        model = PandasModel(df2)
        self.tableWidget.setModel(model)



class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self._data.columns[col]
        return None