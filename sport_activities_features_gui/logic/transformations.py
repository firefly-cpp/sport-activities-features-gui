# NORMALIZACIJA, STANDARDIZACIJA
from scipy.stats import zscore
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class Transformations:
    def __init__(self,user):
        self.user = user
        print("Not implemented")
    
    def one_hot_encoding(df) : 
        return df.join(pd.get_dummies(df['activity_type']))

    def min_max_normalization(self, df : pd.DataFrame)-> pd.DataFrame: 
        temp_df = self.clean_df(df)
        scaler = MinMaxScaler()
        return pd.DataFrame(scaler.fit_transform(temp_df), columns=temp_df.columns)   

    def zscore_normalization(self, df: pd.DataFrame)-> pd.DataFrame: 
        temp_df = self.clean_df(df)
        for column in temp_df :
            temp_df[column] = zscore(temp_df[column]) 
        return temp_df
        
    def log_normalization(self, df: pd.DataFrame)-> pd.DataFrame:
        var = pd.get_dummies(df['activity_type']).columns
        log_df = self.clean_df(df)
        print(log_df) 
        for column in log_df : 
            # usage of the natural logaritem ln 
            if column in var:
                continue
            log_df[column] = np.log(log_df[column])
        return log_df

    def clean_df(self, df: pd.DataFrame) -> pd.DataFrame:
        for column in df:
            column_dtype = str(type(df[column][0]))
            if not ('int' in column_dtype or 'float' in column_dtype) :
                df = df.drop(columns=column)
        for i in range(df.shape[0]) : 
            procent_NaN = (df.loc[[i]].isna().sum().sum() ) / (len(df.columns))
            if procent_NaN > 0.5 : 
                df = df.drop(i)
        # for column in df :
        #     df[column] = df[column].fillna(0)
        return df