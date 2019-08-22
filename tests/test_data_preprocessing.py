import unittest
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