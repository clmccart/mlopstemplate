import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
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

    def test__remove_rows_based_on_col_val__value_not_present__no_change(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        original_df = _get_df(data)
        dp = DataPreprocessor(original_df)
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['Farley'])
        self.assertTrue(returned_df.equals(original_df))
        self.assertTrue(original_df.equals(dp.get_df()))
    
    def test__remove_rows_based_on_col_val__value_present__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['Tom', 'krish', 'jack'], 'Age':[20, 19, 18], 'Type':[1, 2, 1]} 
        original_df = _get_df(data)
        expected_df = _get_df(expected_data)
        dp = DataPreprocessor(original_df)
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['nick'])
        print(returned_df)
        print(expected_df)
        self.assertTrue(returned_df.equals(expected_df))
        self.assertTrue(expected_df.equals(dp.get_df()))
    
    def test__remove_rows_based_on_col__multiple_values__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['krish', 'jack'], 'Age':[19, 18], 'Type':[2, 1]} 
        original_df = _get_df(data)
        expected_df = _get_df(expected_data)
        dp = DataPreprocessor(original_df)
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['nick', 'Tom'])
        print(returned_df)
        self.assertTrue(returned_df.equals(expected_df))
        self.assertTrue(expected_df.equals(dp.get_df()))


def _get_df(data):
    df = pd.DataFrame(data) 
    return df

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
