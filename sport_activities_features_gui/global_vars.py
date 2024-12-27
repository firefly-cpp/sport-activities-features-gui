import os

path = 'store/'


def getStorePath() -> str:    
    return os.path.join(os.getcwd(), path)
