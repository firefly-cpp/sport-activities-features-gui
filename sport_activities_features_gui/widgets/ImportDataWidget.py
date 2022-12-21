from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction, QWidget
from logic.ImportData import ImportData
from models.User import User


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

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_ImportDataWidget(QWidget):
    globalUser: User
    importDataFn: ImportData

    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("ImportData")
        self.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_ImportData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ImportData.setObjectName("lbl_ImportData")
        self.verticalLayout.addWidget(self.lbl_ImportData)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lbl_Output = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_Output.setObjectName("lbl_Output")
        self.verticalLayout.addWidget(self.lbl_Output)
          
        self.pte_Output = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.pte_Output.setEnabled(True)
        self.pte_Output.setObjectName("pte_Output")
        
        self.verticalLayout.addWidget(self.pte_Output)
        self.lbl_ExportRawData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ExportRawData.setObjectName("lbl_ExportRawData")
        self.verticalLayout.addWidget(self.lbl_ExportRawData)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_Csv = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_Csv.setObjectName("btn_Csv")
        self.horizontalLayout.addWidget(self.btn_Csv)
        self.btn_Json = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_Json.setObjectName("btn_Json")
        self.horizontalLayout.addWidget(self.btn_Json)
        self.btn_Pickle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_Pickle.setObjectName("btn_Pickle")
        self.horizontalLayout.addWidget(self.btn_Pickle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        #self.actionOpenFile = QtWidgets.QAction(self)
        #self.actionOpenFile.setObjectName("actionOpenFile")
        
        #self.pushButton.addAction(self.actionOpenFile)
        #self.actionOpenFile.triggered.connect(ImportData.ImportData.openFile())

        self.pushButton.clicked.connect(self.readFiles)
        self.btn_Csv.clicked.connect(self.exportCSV)
        self.btn_Json.clicked.connect(self.exportJSON)
        self.btn_Pickle.clicked.connect(self.exportPickle)
   
    def retranslateUi(self, ImportData):
        _translate = QtCore.QCoreApplication.translate
        ImportData.setWindowTitle(_translate("ImportData", "Form"))
        self.lbl_ImportData.setText(_translate("ImportData", "Import Data:"))
        self.pushButton.setText(_translate("ImportData", "Select folder / file"))
        self.lbl_Output.setText(_translate("ImportData", "Output:"))
        self.lbl_ExportRawData.setText(_translate("ImportData", "Export Raw Data:"))
        self.btn_Csv.setText(_translate("ImportData", "CSV"))
        self.btn_Json.setText(_translate("ImportData", "JSON"))
        self.btn_Pickle.setText(_translate("ImportData", "Pickle"))
    
    def readFiles(self):
        self.importDataFn.openFileDialog(self)
        
    def exportCSV(self):
        self.importDataFn.exportCSV()
        
    def exportJSON(self):
        self.importDataFn.exportJSON()
    
    def exportPickle(self):
        self.importDataFn.exportPickle()
        
    # IMPORT GLOBAL USER
    def importGlobalUser(self, user: User):
        self.globalUser = user
        self.importDataFn = ImportData(user)
        self.OutputExistingData(self.globalUser.data)
        
    def OutputExistingData(self, dataFrame):
        if self.globalUser.data.empty is False :
            
            df2 = dataFrame.copy()
            for column in df2.columns :
                if(df2[column].dtype == type(list)):
                    df2.drop(column, axis=1, inplace=True)
            
            model = PandasModel(df2)
            self.pte_Output.setModel(model)