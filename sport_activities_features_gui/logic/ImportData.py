import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from logic import MultiThread
from sport_activities_features_gui.models.User import User
from widgets import ImportDataWidget
import pandas as pd

class ImportData:
    globalUser: User
    
    def __init__(self, user: User):
        self.globalUser = user
    
    def openFileDialog(self, importDataWidget: ImportDataWidget):
        dialog = FileDialog()
        if dialog.exec_() == dialog.Accepted:
            dirPath = dialog.selectedFiles()
            
            mt = MultiThread.MultiThread()
            data = mt.bulk_load(dirPath[0],4)
            dataFrame = pd.DataFrame(data['data'])
            self.globalUser.saveData(dataFrame)
            
            importDataWidget.OutputExistingData(dataFrame)
    
    def exportCSV(self):
        pd.DataFrame(self.globalUser.data).to_csv('data.csv', index=False)
    
    def exportJSON(self):
        pd.DataFrame(self.globalUser.data).to_json('data.json', orient='records')
        
    def exportPickle(self):
        pd.DataFrame(self.globalUser.data).to_pickle('data.pkl')
    
class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.Directory)
        self.setNameFilters(["TCX Files (*.tcx)"])

    def accept(self):
        super(FileDialog, self).accept()
        
