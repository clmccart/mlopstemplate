import unittest
import pandas as pd
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.data_preprocessing.data_preprocessor import DataPreprocessor

class DataProcessorTests(unittest.TestCase):
    def test__preprocess_empty_df__returns_empty_df(self):
        # Arrange
        dp = DataPreprocessor()
        df = []
        expected_df = []
        # Act
        returned_df = dp.preprocess(df)
        # Assert
        self.assertEqual(expected_df, returned_df)
    
    def test__preprocess_df_no_steps__returns_original_df(self):
        dp = DataPreprocessor()
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        original_df = FakeDataIngestor(data)

        returned_df = dp.preprocess(original_df)

        self.assertEqual(original_df, returned_df)

class FakeDataIngestor:
    def __init__(self, data):
        self.df = pd.DataFrame(data) 

    def get_df(self):
        return self.df