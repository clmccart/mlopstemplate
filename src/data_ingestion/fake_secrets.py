from src.data_ingestion.isecret import iSecret

class FakeSecrets(iSecret):
    def set_up_secrets(self):
        pass
    
    def get_secrets(self):
        pass