import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_preprocessing.data_preprocessor import DataPreprocessor

def _check_equality(df1, df2, dp):
    return (df1.equals(df2) and df2.equals(dp.get_df()))

def _get_df(data):
    df = pd.DataFrame(data) 
    return df

def _setup(data, expected_data):
    original_df = _get_df(data)
    if expected_data == None:
        expected_df = original_df
    else:
        expected_df = _get_df(expected_data)
    dp = DataPreprocessor(original_df)
    return (expected_df, dp)