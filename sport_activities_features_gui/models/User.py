import pandas as pd
import json
class User:
    global username
    global data
    global userPath
    global setting
    
    def __init__(self, _username: str, _data: pd.DataFrame, _userPath: str, _setting: dict):
        self.username = _username
        self.data = _data
        self.userPath =_userPath
        self.setting = _setting
    
    def __init__(self) -> None:
        self.username = ''
        self.data = dict()
        self.userPath = ''
        self.setting = None
    
    def saveData(self):
        try:
            jsonStr = json.dumps(__dict__)
            
        except:
            return 'something went wrong while saving'
    