from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from sport_activities_features_gui.logic.import_data import ImportData
from sport_activities_features_gui.logic.transformations import Transformations
from sport_activities_features_gui.models.user import User
import pandas as pd


class Ui_TransformationsWidget(QWidget):
    globalUser: User
    importDataFn: ImportData
    transformations: Transformations
    refMainWindow = None

    def __init__(self,refMainWindow):
        QWidget.__init__(self)
        self.transformationsFn = None
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.setObjectName("Transformations")
        self.resize(800, 600)
        self.minMaxButton = QtWidgets.QPushButton(self)
        self.minMaxButton.setGeometry(QtCore.QRect(10, 340, 150, 23))
        self.minMaxButton.setObjectName("minMaxButton")
        self.logNormalizationButton = QtWidgets.QPushButton(self)
        self.logNormalizationButton.setGeometry(QtCore.QRect(10, 370, 150, 23))
        self.logNormalizationButton.setObjectName("logNormalizationButton")
        self.zScoreNormalizationButton = QtWidgets.QPushButton(self)
        self.zScoreNormalizationButton.setGeometry(
            QtCore.QRect(10, 400, 150, 23))
        self.zScoreNormalizationButton.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(10, 430, 150, 17))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tableWidget = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.addWidget(self.tableWidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.minMaxButton.pressed.connect(self.minMax)
        self.logNormalizationButton.pressed.connect(self.logNormalization)
        self.zScoreNormalizationButton.pressed.connect(
            self.zScoreNormalization)
        self.refMainWindow = refMainWindow

    def retranslateUi(self, Transformations):
        _translate = QtCore.QCoreApplication.translate
        Transformations.setWindowTitle(_translate("Transformations", "Frame"))
        self.minMaxButton.setText(_translate(
            "Transformations", "Min-Max Normalization"))
        self.logNormalizationButton.setText(
            _translate("Transformations", "Log Normalization"))
        self.zScoreNormalizationButton.setText(
            _translate("Transformations", "Z-Score Normalization"))
        self.checkBox.setText(_translate(
            "Transformations", "One hot encoding"))

    def minMax(self):
        one_hot_encoding = self.checkBox.isChecked()
        transformedData = self.transformationsFn.min_max_normalization(
            self.globalUser.data,one_hot_encoding)
        self.OutPutExistingData(transformedData)
        print("minMax")

    def logNormalization(self):
        one_hot_encoding = self.checkBox.isChecked()
        transformedData = self.transformationsFn.log_normalization(
            self.globalUser.data,one_hot_encoding)
        self.OutPutExistingData(transformedData)

    def zScoreNormalization(self):
        one_hot_encoding = self.checkBox.isChecked()
        transformedData = self.transformationsFn.zscore_normalization(
            self.globalUser.data,one_hot_encoding)
        self.OutPutExistingData(transformedData)

    def importGlobalUser(self, user: User):
        self.globalUser = user
        self.transformationsFn = Transformations(user)
        self.importDataFn = ImportData(user)
        if (self.globalUser.data.empty is False):
            self.OutPutExistingData(self.globalUser.data)

    def OutPutExistingData(self, dataframe: pd.DataFrame):
        df2 = dataframe.copy()

        for column in ['positions', 'altitudes', 'distances', 'timestamps', 'speeds', 'heartrates']:
            if column in df2.columns:
                df2.drop(column, axis=1, inplace=True)

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
