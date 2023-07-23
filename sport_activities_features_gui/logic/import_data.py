import sys
from PyQt6.QtWidgets import QFileDialog
from sport_activities_features_gui.logic.multi_thread import MultiThread
from sport_activities_features_gui.models.user import User
import pandas as pd

class ImportData:
    globalUser: User
    
    def __init__(self, user: User):
        self.globalUser = user
    
    def openFileDialog(self):
        dialog = FileDialog()
        dialog_execution = dialog.exec()
        if dialog_execution == 1:
            
            dirPath = dialog.selectedFiles()
            mt = MultiThread()
            
            #if(len(dirPath) == 1):
                #dataFrame = mt.single_load(dirPath[0])
            #else:
            
            data = mt.bulk_load(dirPath,4)
            dataFrame = pd.DataFrame(data['data'])

            self.globalUser.saveData(dataFrame)
            return dataFrame
        return None

    def exportCSV(self, filePath):
        pd.DataFrame(self.globalUser.data).to_csv(filePath, index=False)
    
    def exportJSON(self, filePath):
        pd.DataFrame(self.globalUser.data).to_json(filePath, orient='records')
        
    def exportPickle(self, filePath):
        pd.DataFrame(self.globalUser.data).to_pickle(filePath)
    
class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.options(self).DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilters(["TCX Files (*.tcx)"])

    def accept(self):
        super(FileDialog, self).accept()
        
