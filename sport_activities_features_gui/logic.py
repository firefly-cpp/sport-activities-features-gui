from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QAction
from widgets.ImportData import Ui_ImportData
from config import app, ui_mainWindow, ui_importData

def quit():
    qApp.quit()
    
## TODO: Fix this function 
def setImportData():
    ui_importData = Ui_ImportData()
    ui_mainWindow.mainLayout.addWidget(ui_importData)
    ui_mainWindow.mainLayout.show()
    ui_importData.show()
    