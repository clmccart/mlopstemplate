from src.data_ingestion.isecret import iSecret
import json

class SecretJSON(iSecret):

    def set_up_secrets(self):
        with open("secrets.json") as json_file:
            secrets = json.load(json_file)
        self.blob_secrets = secrets['blob']
    
    def get_secrets(self):
        return self.blob_secrets