import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_ingestion.data_ingestion import DataIngestor
from utils.utils import _setup_dataingestor, _check_equality


class MockBlockBlobService:
    def __init__(self, account_name, account_key):
        pass

    def list_blobs(self, container_name):
        blob1 = MockBlob(name="file1")
        blob2 = MockBlob(name="file2")
        blob3 = MockBlob(name="file3")
        self.list_of_blobs =[blob1, blob2, blob3]
        return self.list_of_blobs

    def get_blob_to_text(self, container_name, blob_name):
        mocktext = MockText("some text")
        return MockText

class MockBlob:
    def __init__(self, name):
        self.name = name

class MockText:
    def __init__(self, text):
        self.content = text


class DataIngestorClass(unittest.TestCase):

    def test__filename_doesnt_exist__throws_error(self):
        di = DataIngestor(desired_file=None, secrets_path="secrets.json", service=MockBlockBlobService)
        di.set_up_secrets()
        di.connect_to_blob()
        self.assertRaises(FileNotFoundError, di.pull_file)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
