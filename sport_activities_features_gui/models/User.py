import pickle
import pandas as pd
import json
from GlobalVars import *
import os

class User:
    global username
    global data
    global userPath
    global setting
    
    def __init__(self) -> None:
        self.username = ''
        self.data = dict()
        self.userPath = ''
        self.setting = None
        
    def __init1__(self, _username: str, _setting: dict):
        self.username = _username
        currentPath = os.getcwd()
        self.userPath = str(currentPath + path + _username + '/')
        self.setting = _setting
        User.checkForExistingData(self.userPath)
   
    # creates directory in store
    def checkForExistingData(userPath):
        if not os.path.isdir(userPath):
            os.makedirs(userPath)
        found = 0
        with os.scandir(userPath) as entries:
            for entry in entries:
                if entry.name == 'data.pickle':
                    User.loadData(userPath)
        if(found == 0):
            User.saveData(userPath, [])

    def saveData(userPath, data):
        pickleFile = open(userPath+'data.pickle', 'wb')
        pickle.dump(data, pickleFile)
        pickleFile.close()
        return data
        
    def loadData(userPath):
        pickleFile = open(userPath+'data.pickle', 'rb')
        data = pickle.load(pickleFile)
        pickleFile.close()
        return data
             
