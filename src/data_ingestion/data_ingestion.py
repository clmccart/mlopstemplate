import os
import string
from azure.storage.blob import BlockBlobService
import json    
from io import StringIO
import pandas as pd
import glob 
 
class DataIngestor:
    def __init__(self, desired_file, secrets_path=None, service=BlockBlobService):
        self.service = service
        self.secrets_path = secrets_path
         
        self.desired_file = desired_file   

    def set_up_secrets(self):
        # check to see if secrets.json path exists, if not, try to grab from env variables
        if not (os.path.isfile(self.secrets_path)):
            self.blob_secrets = self.get_secrets_from_env()
        else:
            with open(self.secrets_path) as json_file:
                secrets = json.load(json_file)
            self.blob_secrets = secrets['blob']
    
    def get_secrets_from_env(self):
        blob_secrets = {
                        "account_name": os.environ['ACCOUNTNAME'],
                        "account_key" : os.environ['ACCOUNTKEY'],
                        "container_name": os.environ['CONTAINERNAME']
                        }
        
        return blob_secrets

    def connect_to_blob(self):
        self.block_blob_service = self.service(account_name=self.blob_secrets['account_name'], 
                                                account_key=self.blob_secrets['account_key'])
        self.container_name = self.blob_secrets['container_name']
        print(self.container_name)
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
                return
        raise FileNotFoundError('no file with the name {} was found'.format(self.desired_file))
    
    def get_df(self):
        self.set_up_secrets()
        self.connect_to_blob()
        self.pull_file()
        return self.df







