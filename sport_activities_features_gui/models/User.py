import pandas as pd
import json
class User:
    def __init__(self, _username: str, _data: pd.DataFrame, _userPath: str, _setting: dict):
        self.username = _username
        self.data = _data
        self.userPath =_userPath
        self.setting = _setting
    def saveData(self):
        try:
            jsonStr = json.dumps(__dict__)
            
        except:
            return 'something went wrong while saving'
    