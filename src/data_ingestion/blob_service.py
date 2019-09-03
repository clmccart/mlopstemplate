from azure.storage.blob import BlockBlobService
from src.data_ingestion.iservice import iService
import pandas as pd
from io import StringIO


class BlobService(iService):

    def get_df(self):
        self.connect_to_blob()
        self.pull_file()
        return self.df
    
    
    def connect_to_blob(self):
        self.block_blob_service = BlockBlobService(account_name=self.secrets.get_account_name(), 
                                                    account_key=self.secrets.get_account_key())
        self.container_name = self.secrets.get_container_name()
        self.generator = self.block_blob_service.list_blobs(self.container_name)
        print("Connected to Blob Successfully")
    
    def pull_file(self):
        for blob in self.generator:
            if blob.name == self.desired_file:
                print("Pulling " + blob.name + ". . .")
                blobstring = self.block_blob_service.get_blob_to_text(self.container_name, blob.name).content
                df = pd.read_csv(StringIO(blobstring))
                print("Pull complete.")
                self.df = df
                return
        raise FileNotFoundError('no file with the name {} was found'.format(self.desired_file))