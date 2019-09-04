from azure.storage.blob import BlockBlobService
from src.data_ingestion.services.iservice import iService
import pandas as pd
from io import StringIO

class BlobService(iService):
    def __init__(self, desired_file, secret_provider):
        super().__init__(desired_file, secret_provider)
        self.container_name = self.secret_provider.secrets['container_name']    

    def get_df(self):
        try:
            self.connect_to_service()
            self.locate_desired_file()
            self.download_file_as_df()
            return self.df
        except:
            raise Exception('Was not able to return a dataframe.')
    
    def connect_to_service(self):
        try:
            self.block_blob_service = BlockBlobService(account_name=self.secret_provider.secrets['account_name'], 
                                                        account_key=self.secret_provider.secrets['account_key'])
            self.container = self.block_blob_service.list_blobs(self.container_name)
        except:
            raise Exception('Unable to authenticate with provided secrets. Account name or key is incorrect')
    
    def locate_desired_file(self):
        try:
            container = self.block_blob_service.list_blobs(self.container_name)
            for blob in container:
                    if blob.name == self.desired_file:
                        print("Pulling " + blob.name + ". . .")
                        self.location = blob.name
        except:
            raise Exception("Unable to locate the desired file.")
    
    def download_file_as_df(self):
        blobstring = self.block_blob_service.get_blob_to_text(self.container_name, self.location).content
        self.df = pd.read_csv(StringIO(blobstring))
 