import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_ingestion.data_ingestion import DataIngestor
from src.data_ingestion.services.blob_service import BlobService
from tests.fakedata.fake_secrets import FakeSecrets
from src.data_ingestion.secretproviders.secret_json_handler import SecretJSON

class TestBlobService(unittest.TestCase):

    def test__connect_to_service__bad_secrets__throws_error(self):
        # Arrange
        service = BlobService(desired_file="foo.csv",
                                secret_provider=FakeSecrets)
        # Act / Assert
        self.assertRaisesWithMessage(msg="Unable to authenticate with provided secrets.",
                                    func=service.connect_to_service)

    def test__get_df__fails__throws_error(self):
        service = BlobService(desired_file="foo.csv",
                                secret_provider=FakeSecrets)
        self.assertRaisesWithMessage(msg="Was not able to return a dataframe.",
                                    func=service.get_df)

    def test__locate_file__fails__throws_error(self):
        service = BlobService(desired_file="foo.csv",
                                secret_provider=FakeSecrets)
        self.assertRaisesWithMessage(msg="Unable to locate the desired file.",
                                    func=service.locate_desired_file)

    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertTrue(msg in str(inst))

    # Integration tests
    @unittest.skip("this is an integration test")
    def test__pull_file__desired_file_does_not_exist__throws_error(self):
        service = BlobService(desired_file="notarealfilename.csv",
                                secret_provider=SecretJSON)
        service.connect_to_blob()
        with self.assertRaises(FileNotFoundError):
            service.pull_file()
    
    @unittest.skip("this is an integration test")
    def test__valid_args__returns_expected_df(self):
        pass

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

