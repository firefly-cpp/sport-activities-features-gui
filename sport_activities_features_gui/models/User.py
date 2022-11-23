import pandas as pd
class User:
    def __init__(self, _username: str, _data: pd.DataFrame, _pathToData: str, _setting: dict):
        username = _username
        data = _data
        pathToData =_pathToData
        setting = _setting