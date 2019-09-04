from src.data_ingestion.secretproviders.isecret import iSecret
import json

class SecretJSON(iSecret):

    def set_up_secrets(self):
        try:
            with open("secrets.json") as json_file:
                secrets = json.load(json_file)
            self.secrets = secrets['blob']
        except:
            raise Exception('Was unable to access the secrets.json file')
    
    