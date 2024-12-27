import sys
from PyQt6.QtWidgets import QFileDialog
from sport_activities_features_gui.logic.multi_thread import MultiThread
from sport_activities_features_gui.models.user import User
from sport_activities_features.tcx_manipulation import TCXFile
import pandas as pd


class ImportData:
    """This class imports data from a file and exports data to a file."""
    globalUser: User

    def __init__(self, user: User):        
        self.globalUser = user

    def openFolderDialog(self):
        """This function opens a folder dialog to select a folder to import.\n
        Returns:
            DataFrame: The data from the files in the folder.
        """
        dialog = FolderDialog()
        dialog_execution = dialog.exec()
        if dialog_execution == 1:
            selectedFolderPath = dialog.selectedFiles()[0]
            tcx_file = TCXFile()
            selectedFilePaths = tcx_file.read_directory(selectedFolderPath)
            mt = MultiThread()
            
            data = mt.bulk_load(selectedFilePaths, 4)
            dataFrame = pd.DataFrame(data['data'])

            self.globalUser.saveData(dataFrame)
            return dataFrame
        return None
    
    def openFileDialog(self):
        """This function opens a file dialog to select a file to import.\n
        Returns:
            DataFrame: The data from the file.        
        """
        dialog = FileDialog()
        dialog_execution = dialog.exec()
        if dialog_execution == 1:
            selectedFilePaths = dialog.selectedFiles()
            mt = MultiThread()

            data = mt.bulk_load(selectedFilePaths, 4)
            dataFrame = pd.DataFrame(data['data'])

            self.globalUser.saveData(dataFrame)
            return dataFrame
        return None

    def exportCSV(self, filePath):
        """This function exports the data to a CSV file.\n
        Args:
            filePath (str): The file path to export the data.
        """
        pd.DataFrame(self.globalUser.data).to_csv(filePath, index=False)

    def exportJSON(self, filePath):
        """This function exports the data to a JSON file.\n
        Args:
            filePath (str): The file path to export the data.
        """
        pd.DataFrame(self.globalUser.data).to_json(filePath, orient='records')

    def exportPickle(self, filePath):
        """This function exports the data to a pickle file.\n
        Args:
            filePath (str): The file path to export the data.
        """
        pd.DataFrame(self.globalUser.data).to_pickle(filePath)


class FileDialog(QFileDialog):
    """This class creates a file dialog to select a file to import."""
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.options(self).DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilters(["TCX Files (*.tcx)"])

    def accept(self):
        super(FileDialog, self).accept()

class FolderDialog(QFileDialog):
    """This class creates a folder dialog to select a folder to import."""
    def __init__(self, *args, **kwargs):
        super(FolderDialog, self).__init__(*args, **kwargs)
        self.setOption(QFileDialog.options(self).DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.FileMode.Directory)        

    def accept(self):
        super(FolderDialog, self).accept()