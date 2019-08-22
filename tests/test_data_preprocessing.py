import unittest
import pandas as pd
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.data_preprocessing.data_preprocessor import DataPreprocessor

class DataProcessorTests(unittest.TestCase):
    
    def test__preprocess_df_no_steps__returns_original_df(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        original_df = _get_df(data)
        dp = DataPreprocessor(original_df)

        returned_df = dp.donothing()

        self.assertTrue(original_df.equals(returned_df))
    
    def test__drop_one_column__drops_one_column(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        expected_data = {'Age':[20, 21, 19, 18]} 
        original_df = _get_df(data)
        expected_df = _get_df(expected_data)
        dp = DataPreprocessor(original_df)
        returned_df = dp.drop_columns('Name')
        self.assertTrue(returned_df.equals(expected_df))
        self.assertTrue(expected_df.equals(dp.get_df()))

    
    def test__drop_list_of_columns__drops_columns(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Type':[1, 0, 2, 1]} 
        original_df = _get_df(data)
        expected_df = _get_df(expected_data)
        dp = DataPreprocessor(original_df)
        returned_df = dp.drop_columns(['Name', 'Age'])
        self.assertTrue(returned_df.equals(expected_df))
        self.assertTrue(expected_df.equals(dp.get_df()))

def _get_df(data):
    df = pd.DataFrame(data) 
    return df
