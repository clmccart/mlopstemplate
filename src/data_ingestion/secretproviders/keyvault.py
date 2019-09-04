from src.data_ingestion.secretproviders.isecret import iSecret

class KeyVaultProvider(iSecret):
    
    def set_up_secrets(self):
        self.secrets = {}