import unittest
import pandas as pd
import sys
import os
from src.data_preprocessing.data_preprocessor import DataPreprocessor
from src.data_preprocessing.steps.drop_columns import DropColumnsStep
from src.data_preprocessing.steps.row_bc_col import RemoveRowBcColStep

class DataProcessorTests(unittest.TestCase):
    
    def test__preprocess_df_no_steps__returns_original_df(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        original_df = pd.DataFrame(data)

        preprocessor = DataPreprocessor(original_df)

        returned_df = preprocessor.preprocess()

        self.assertTrue(returned_df.equals(original_df))

    def test__drop_one_column__drops_one_column(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        expected_data = {'Age':[20, 21, 19, 18]} 
        expected_df = pd.DataFrame(expected_data)
        original_df = pd.DataFrame(data)
        steps = [DropColumnsStep('Name')]
        preprocessor = DataPreprocessor(original_df, steps)

        returned_df = preprocessor.preprocess()

        self.assertTrue(returned_df.equals(expected_df))
    
    def test__drop_list_of_columns__drops_columns(self):
        # Arrange
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Type':[1, 0, 2, 1]} 
        original_df = pd.DataFrame(data)
        expected_df = pd.DataFrame(expected_data)
        steps = [DropColumnsStep(column_names=['Name', 'Age'])]
        preprocessor = DataPreprocessor(original_df, steps)
        # Act
        returned_df = preprocessor.preprocess()
        # Assert
        self.assertTrue(returned_df.equals(expected_df))

    def test__multiple_steps_returns_as_expected(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Type':[2]} 
        expected_df = pd.DataFrame(expected_data)
        original_df = pd.DataFrame(data)
        
        step1 = RemoveRowBcColStep(column_name='Name', bad_values=['nick', 'Tom', 'jack'])
        step2 = DropColumnsStep(column_names=['Name', 'Age'])
        steps = [step1, step2]

        preprocessor = DataPreprocessor(original_df, steps)
        
        returned_df = preprocessor.preprocess()

        self.assertTrue(returned_df.equals(expected_df))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
