import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_ingestion.data_ingestion import DataIngestor
from tests.fakedata.fake_service import FakeService
from tests.fakedata.fake_secrets import FakeSecrets

# change this to an abstract base class called "service" or something
# it should contain only the functions that your are going to call which should really just be wrappers
# create a class that inherits from it called a fake for testing, a real one for blob

class TestDataIngestor(unittest.TestCase):

    def test__filename_doesnt_exist__throws_error(self):
        self.assertRaisesWithMessage(msg='desired_file is None.', 
                                    func= DataIngestor,
                                    desired_file=None, 
                                    secret_provider=None, 
                                    service=FakeService)

    def test__secret_provider_is_none__throws_error(self):
        self.assertRaisesWithMessage(msg='secret_provider is None.', 
                                    func= DataIngestor,
                                    desired_file="foo.csv", 
                                    secret_provider=None, 
                                    service=FakeService)
    
    def test__valid_args__get_df__returns_df(self):
        # Arrange
        ingestor = DataIngestor(desired_file="foo.txt",
                                secret_provider=FakeSecrets,
                                service=FakeService)
        # Act
        df = ingestor.get_df()
        # Assert
        self.assertFalse(df.empty)

    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertTrue(msg in str(inst))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

