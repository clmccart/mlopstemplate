from src.data_ingestion.isecret import iSecret
import json

class SecretJSON(iSecret):

    def set_up_secrets(self):
        with open("secrets.json") as json_file:
            secrets = json.load(json_file)
        self.blob_secrets = secrets['blob']
    
    def get_account_name(self):
        return self.blob_secrets['account_name']
    
    def get_account_key(self):
        return self.blob_secrets['account_key']
    
    def get_container_name(self):
        return self.blob_secrets['container_name']