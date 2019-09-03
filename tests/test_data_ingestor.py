import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_ingestion.data_ingestion import DataIngestor
from src.data_ingestion.fake_service import FakeService

# change this to an abstract base class called "service" or something
# it should contain only the functions that your are going to call which should really just be wrappers
# create a class that inherits from it called a fake for testing, a real one for blob

class TestDataIngestorClass(unittest.TestCase):

    def test__filename_doesnt_exist__throws_error(self):
        self.assertRaises(FileNotFoundError, DataIngestor(desired_file=None, secret_provider=None, service=FakeService))

    def test__fake(self):
        self.assertTrue(True)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
