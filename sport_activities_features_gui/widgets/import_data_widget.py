from sport_activities_features_gui.models import User
from sport_activities_features_gui.logic.import_data import ImportData

import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QPushButton, QLabel, QTableView, QHBoxLayout, QSpacerItem, QSizePolicy

from PyQt6 import sip
from PyQt6.QtCore import Qt
# Rest of the code

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
        if orientation == Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_ImportDataWidget(QWidget):
    globalUser: User
    importDataFn: ImportData
    refMainWindow = None

    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("ImportData")
        self.resize(800, 600)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_ImportData = QLabel(self.verticalLayoutWidget)
        self.lbl_ImportData.setObjectName("lbl_ImportData")
        self.verticalLayout.addWidget(self.lbl_ImportData)
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lbl_Output = QLabel(self.verticalLayoutWidget)
        self.lbl_Output.setObjectName("lbl_Output")
        self.verticalLayout.addWidget(self.lbl_Output)
          
        self.pte_Output = QTableView(self.verticalLayoutWidget)
        self.pte_Output.setEnabled(True)
        self.pte_Output.setObjectName("pte_Output")
        self.verticalLayout.addWidget(self.pte_Output)
        
        self.lbl_ExportRawData = QLabel(self.verticalLayoutWidget)
        self.lbl_ExportRawData.setObjectName("lbl_ExportRawData")
        self.verticalLayout.addWidget(self.lbl_ExportRawData)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_Csv = QPushButton(self.verticalLayoutWidget)
        self.btn_Csv.setObjectName("btn_Csv")
        self.horizontalLayout.addWidget(self.btn_Csv)
        self.btn_Json = QPushButton(self.verticalLayoutWidget)
        self.btn_Json.setObjectName("btn_Json")
        self.horizontalLayout.addWidget(self.btn_Json)
        self.btn_Pickle = QPushButton(self.verticalLayoutWidget)
        self.btn_Pickle.setObjectName("btn_Pickle")
        self.horizontalLayout.addWidget(self.btn_Pickle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.readFiles)
        self.btn_Csv.clicked.connect(self.exportCSV)
        self.btn_Json.clicked.connect(self.exportJSON)
        self.btn_Pickle.clicked.connect(self.exportPickle)
   
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ImportData", "Form"))
        self.lbl_ImportData.setText(_translate("ImportData", "Import Data:"))
        self.pushButton.setText(_translate("ImportData", "Select folder / file"))
        self.lbl_Output.setText(_translate("ImportData", "Output:"))
        self.lbl_ExportRawData.setText(_translate("ImportData", "Export Raw Data:"))
        self.btn_Csv.setText(_translate("ImportData", "CSV"))
        self.btn_Json.setText(_translate("ImportData", "JSON"))
        self.btn_Pickle.setText(_translate("ImportData", "Pickle"))
    
    def readFiles(self):
        df = self.importDataFn.openFileDialog()
        if(df is not None):
            self.OutputExistingData(df)
            self.refreshCalendarWidget()
        # Refresh calendar widget

    def saveFileDialog(self, defaultFileName, fileFormat):
        fd = QFileDialog()
        fd.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        fileName, _ = fd.getSaveFileName(self,"QFileDialog.getSaveFileName()",defaultFileName, fileFormat)
        return fileName
    
    def exportCSV(self):
        filePath = self.saveFileDialog("data.csv", "CSV File (*.csv)")
        if(filePath != '' and filePath != None): 
            self.importDataFn.exportCSV(filePath)
        
    def exportJSON(self):
        filePath = self.saveFileDialog("data.json", "Json File (*.json)")
        if(filePath != '' and filePath != None): 
            self.importDataFn.exportJSON(filePath)
    
    def exportPickle(self):
        filePath = self.saveFileDialog("data.pickle", "Pickle File (*.pickle)")
        if(filePath != '' and filePath != None): 
            self.importDataFn.exportPickle(filePath)
        
    # IMPORT GLOBAL USER
    def importGlobalUser(self, user: User):
        self.globalUser = user
        self.importDataFn = ImportData(user)
        self.OutputExistingData(self.globalUser.data)
        
    def OutputExistingData(self, dataFrame):
        if self.globalUser.data.empty is False:
            
            df2 = dataFrame.copy()
            # for column in df2.columns :
            #     if(df2[column] != None):
            #         if(df2[column].dtype == type(list)):
            #             df2 = df2.drop(column, axis=1, inplace=True)
            df2 = df2.drop(columns=['positions', 'altitudes', 'distances', 'timestamps', 'speeds','heartrates'])
            model = PandasModel(df2)
            self.pte_Output.setModel(model)
        
    def refreshCalendarWidget(self):
        self.refMainWindow.mainLayout_4.removeWidget(self.refMainWindow.calendarUi)
        sip.delete(self.refMainWindow.calendarUi)
        self.refMainWindow.calendarUi = None
        self.refMainWindow.calendarUi = Ui_ImportDataWidget()
        self.refMainWindow.mainLayout_4.addWidget(self.refMainWindow.calendarUi)
        self.refMainWindow.calendarUi.importGlobalUser(self.globalUser)