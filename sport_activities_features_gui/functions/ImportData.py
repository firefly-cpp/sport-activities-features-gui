import sys
from PyQt5.QtWidgets import QFileDialog
from functions import MultiThread
from sport_activities_features_gui.models.User import User
import widgets.ImportData as ImportData
import pandas as pd
from GlobalVars import *

class ImportData:
    
    def __init__(self):
        pass
    
    @staticmethod
    def openFileDialog(ImportData: ImportData):
        dialog = FileDialog()
        if dialog.exec_() == dialog.Accepted:
            dirPath = dialog.selectedFiles()
            
            mt = MultiThread.MultiThread()
            data = mt.bulk_load(dirPath[0],4)
            User.data = data # tukaj ni vrednosti v User.data global variablu
            
            ImportData.pte_Output.clear()
            ImportData.pte_Output.appendPlainText('Num Of Files: ' + str(User.data['numOfFiles']))
            ImportData.pte_Output.appendPlainText('Num Of Error Files: ' + str(User.data['numOfFilesNotRead']))
            ImportData.pte_Output.appendPlainText(str(User.data['data']))
    
    def exportCSV():
        pd.DataFrame(User.data['data']).to_csv('data.csv', index=False)
    
    def exportJSON():
        pd.DataFrame(User.data['data']).to_json('data.json', orient='records')
        
    def exportPickle():
        pd.DataFrame(User.data['data']).to_pickle('data.pkl')
    
class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.Directory)
        self.setNameFilters(["TCX Files (*.tcx)"])

    def accept(self):
        super(FileDialog, self).accept()
        
