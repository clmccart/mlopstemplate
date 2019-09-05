import unittest
from src.data_preprocessing.steps.row_bc_col import RemoveRowBcColStep
import pandas as pd 

class RRCBRStepTests(unittest.TestCase):
    
    def test__no_col__throws_error(self):
        self.assertRaises(Exception, RemoveRowBcColStep(column_name=None, bad_values="some bad values"))

    def test__no_bad_values__throws_error(self):
        self.assertRaises(Exception, RemoveRowBcColStep(column_name="some column", bad_values=None))

    def test__remove_rows_based_on_col__multiple_values__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['krish', 'jack'], 'Age':[19, 18], 'Type':[2, 1]} 
        expected_df = pd.DataFrame(expected_data)
        original_df = pd.DataFrame(data)
        
        step = RemoveRowBcColStep(column_name='Name', bad_values=['nick', 'Tom'])

        returned_df = step.run_step(original_df)

        self.assertTrue(returned_df.equals(expected_df))

    def test__remove_rows_based_on_col_val__value_present__is_removed(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Name':['Tom', 'krish', 'jack'], 'Age':[20, 19, 18], 'Type':[1, 2, 1]} 
        expected_df = pd.DataFrame(expected_data)
        original_df = pd.DataFrame(data)
        
        step = RemoveRowBcColStep(column_name='Name', bad_values=['nick'])
        
        returned_df = step.run_step(original_df)

        self.assertTrue(returned_df.equals(expected_df))
    
    def test__remove_rows_based_on_col_val__value_not_present__no_change(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        original_df = pd.DataFrame(data)
        step = RemoveRowBcColStep(column_name='Name', bad_values='Farley')
        
        returned_df = step.run_step(original_df)
        
        self.assertTrue(returned_df.equals(original_df))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))