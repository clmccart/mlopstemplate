import os
import string
from azure.storage.blob import BlockBlobService
import json    
from io import StringIO
import pandas as pd
import glob 
class DataIngestor:
    def __init__(self, deseried_file, secrets_path):
        self.secrets_path = secrets_path
        self.desired_file = deseried_file

        self.set_up_secrets()
        self.connect_to_blob()
        self.pull_file()    

    def set_up_secrets(self):
        with open(self.secrets_path) as json_file:
            secrets = json.load(json_file)
        self.blob_secrets = secrets['blob']

    def connect_to_blob(self):
        self.block_blob_service = BlockBlobService(account_name=self.blob_secrets['account_name'], 
                                                    account_key=self.blob_secrets['account_key'])
        self.container_name = self.blob_secrets['container_name']
        self.generator = self.block_blob_service.list_blobs(self.container_name)

    def pull_file(self):
        for blob in self.generator:
            if blob.name == self.desired_file:
                print("\t Pulling " + blob.name + ". . .")
                blobstring = self.block_blob_service.get_blob_to_text(self.container_name, blob.name).content
                df = pd.read_csv(StringIO(blobstring))
                print("Pull complete.")
                print(df.head())
                self.df = df
    
    def get_df(self):
        return self.df







