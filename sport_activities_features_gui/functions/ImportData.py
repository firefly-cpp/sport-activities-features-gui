import sys
from PyQt5.QtWidgets import QFileDialog
from functions import MultiThread
import widgets.ImportData as ImportData

class ImportData:
    
    global dirPath
    global data
    
    def __init__(self):
        pass
    
    @staticmethod
    def openFileDialog(ImportData: ImportData):
        dialog = FileDialog()
        if dialog.exec_() == dialog.Accepted:
            dirPath = dialog.selectedFiles()
            
            mt = MultiThread.MultiThread()
            data = mt.bulk_load(dirPath[0],4)
            
            ImportData.pte_Output.clear()
            ImportData.pte_Output.appendPlainText('Num Of Files: ' + str(data['numOfFiles']))
            ImportData.pte_Output.appendPlainText('Num Of Not Read Files: ' + str(data['numOfFilesNotRead']))
            ImportData.pte_Output.appendPlainText(str(data['data']))

    
class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.Directory)
        self.setNameFilters(["TCX Files (*.tcx)"])

    def accept(self):
        super(FileDialog, self).accept()
        
