import unittest
import pandas as pd
import sys
import os
from utils.utils import _setup, _check_equality

class DataProcessorTests(unittest.TestCase):
    
    def test__preprocess_df_no_steps__returns_original_df(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        expected_df, dp = _setup(data, expected_data=None)

        returned_df = dp.donothing()

        self.assertTrue(_check_equality(returned_df, expected_df, dp))

    def test__drop_one_column__drops_one_column(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
        expected_data = {'Age':[20, 21, 19, 18]} 
        expected_df, dp = _setup(data, expected_data)
        
        returned_df = dp.drop_columns('Name')
        
        self.assertTrue(_check_equality(returned_df, expected_df, dp))
    
    def test__drop_list_of_columns__drops_columns(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Type':[1, 0, 2, 1]} 
        expected_df, dp = _setup(data, expected_data)
        
        returned_df = dp.drop_columns(['Name', 'Age'])
        
        self.assertTrue(_check_equality(returned_df, expected_df, dp))

    def test__remove_rows_based_on_col_val__value_not_present__no_change(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_df, dp = _setup(data, expected_data=None)
        
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['Farley'])
        
        self.assertTrue(_check_equality(returned_df, expected_df, dp))
    
    def test__remove_rows_based_on_col_val__value_present__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['Tom', 'krish', 'jack'], 'Age':[20, 19, 18], 'Type':[1, 2, 1]} 
        expected_df, dp = _setup(data, expected_data)
        
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['nick'])
        
        self.assertTrue(_check_equality(returned_df, expected_df, dp))

    def test__remove_rows_based_on_col__multiple_values__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['krish', 'jack'], 'Age':[19, 18], 'Type':[2, 1]} 
        expected_df, dp = _setup(data, expected_data)
        
        returned_df = dp.remove_rows_based_on_value(column_name='Name', bad_values=['nick', 'Tom'])

        self.assertTrue(_check_equality(returned_df, expected_df, dp))

    def test__supposed_to_fail(self):
        self.assertTrue(False)
        
if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
