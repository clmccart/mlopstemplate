import unittest
from src.data_preprocessing.steps.drop_columns import DropColumnsStep
import pandas as pd 

class DropColStepTests(unittest.TestCase):
    
    def test__no_col__throws_error(self):
        self.assertRaises(Exception, DropColumnsStep(column_names=None))

    def test__one_column__drops_one_col(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        original_df = pd.DataFrame(data)
        expected_data = {'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_df = pd.DataFrame(expected_data)
        step = DropColumnsStep(column_names="Name")
        returned_df = step.run_step(original_df)
        self.assertTrue(returned_df.equals(expected_df))
    
    def test__list_of_columns__drops_columns(self):
        # Arrange
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Type':[1, 0, 2, 1]} 
        expected_data = {'Type':[1, 0, 2, 1]} 
        original_df = pd.DataFrame(data)
        expected_df = pd.DataFrame(expected_data)
        step = DropColumnsStep(column_names=['Name', 'Age'])
        # Act
        returned_df = step.run_step(original_df)
        # Assert
        self.assertTrue(returned_df.equals(expected_df))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))