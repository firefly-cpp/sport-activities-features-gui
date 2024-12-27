# NORMALIZACIJA, STANDARDIZACIJA
from scipy.stats import zscore
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class Transformations:
    """This class handles the normalization and standardization of the data."""
    def __init__(self, user):
        self.user = user        

    def one_hot_encoding(self,df):
        """This function performs one-hot encoding on the data.\n
        Args:
            df (DataFrame): The data to encode.
        Returns:
            DataFrame: The encoded data.
        """
        return df.join(pd.get_dummies(df['activity_type']))

    def min_max_normalization(self, df: pd.DataFrame, one_hot_encoding: bool) -> pd.DataFrame:
        """This function performs min-max normalization on the data.\n
        Args:
            df (DataFrame): The data to normalize.
            one_hot_encoding (bool): Whether to perform one-hot encoding.
        Returns:
            DataFrame: The normalized data.
        """
        temp_df = self.clean_df(df)
        scaler = MinMaxScaler()
        activity_types = df['activity_type']
        new_df = pd.DataFrame(scaler.fit_transform(temp_df), columns=temp_df.columns)
        new_df.insert(0, 'activity_type', activity_types)
        if one_hot_encoding:
            new_df = self.one_hot_encoding(new_df)
            new_df = new_df.drop(columns='activity_type')
        return new_df

    def zscore_normalization(self, df: pd.DataFrame, one_hot_encoding: bool) -> pd.DataFrame:
        """This function performs z-score normalization on the data.\n
        Args:
            df (DataFrame): The data to normalize.
            one_hot_encoding (bool): Whether to perform one-hot encoding.
        Returns:
            DataFrame: The normalized data.
        """        
        temp_df = self.clean_df(df)
        for column in temp_df:
            temp_df[column] = zscore(temp_df[column])
        activity_types = df['activity_type']
        new_df = temp_df
        new_df.insert(0, 'activity_type', activity_types)
        if one_hot_encoding:
            new_df = self.one_hot_encoding(new_df)
            new_df = new_df.drop(columns='activity_type')
        return new_df

    def log_normalization(self, df: pd.DataFrame, one_hot_encoding: bool) -> pd.DataFrame:
        """This function performs logarithmic normalization on the data.\n
        Args:
            df (DataFrame): The data to normalize.
            one_hot_encoding (bool): Whether to perform one-hot encoding.
        Returns:
            DataFrame: The normalized data.
        """
        var = pd.get_dummies(df['activity_type']).columns
        log_df = self.clean_df(df)
        print(log_df)
        for column in log_df:
            # usage of the natural logarithm ln
            if column in var:
                continue
            log_df[column] = np.log(log_df[column])
            
        activity_types = df['activity_type']
        new_df = log_df
        new_df.insert(0, 'activity_type', activity_types)
        if one_hot_encoding:
            new_df = self.one_hot_encoding(new_df)
            new_df = new_df.drop(columns='activity_type')
        return new_df

    def clean_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """This function cleans the data by removing NaN values and non-numeric columns.\n
        Args:
            df (DataFrame): The data to clean.
        Returns:
            DataFrame: The cleaned data.
        """
        for column in df:
            column_dtype = str(type(df[column][0]))
            if not ('int' in column_dtype or 'float' in column_dtype):
                df = df.drop(columns=column)
        for i in range(df.shape[0]):
            procent_NaN = (df.loc[[i]].isna().sum().sum()) / (len(df.columns))
            if procent_NaN > 0.5:
                df = df.drop(i)
        return df
