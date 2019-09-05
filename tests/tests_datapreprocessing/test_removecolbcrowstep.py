import unittest
from src.data_preprocessing.steps.row_bc_col import RemoveRowBcColStep

class RRCBRStep(unittest.TestCase):
    
    def test__no_row__throws_error(self):
        self.assertTrue(False)



if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))