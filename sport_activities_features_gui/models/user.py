import pickle
import pandas as pd
import os
from ..global_vars import *


def initGlobalUser(userName, settings):
    global user
    user = User(userName, settings)
    return user

class User:
    global username
    global data
    global userPath
    global setting
        
    def __init__(self, _username: str, _setting: dict):
        self.username: str = _username
        self.userPath: str = str(getStorePath() + _username + '/')
        self.setting: dict = _setting
        self.checkForExistingData()
   
    # creates directory in store
    def checkForExistingData(self):
        if not os.path.isdir(self.userPath):
            os.makedirs(self.userPath)
        found = 0
        with os.scandir(self.userPath) as entries:
            for entry in entries:
                if entry.name == 'data.pickle':
                    self.loadData()
                    found = 1
        if not found:
            self.saveData(pd.DataFrame())

    def saveData(self, data: pd.DataFrame):
        pickleFile = open(self.userPath+'data.pickle', 'wb')
        pickle.dump(data, pickleFile)
        pickleFile.close()
        self.data: pd.DataFrame = data
        
    def loadData(self):
        pickleFile = open(self.userPath+'data.pickle', 'rb')
        self.data: pd.DataFrame = pickle.load(pickleFile)
        pickleFile.close()
             
