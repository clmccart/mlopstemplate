from src.data_ingestion.secretproviders.isecret import iSecret

class FakeSecrets(iSecret):
    def set_up_secrets(self):
        fake_secrets = {"account_name": "bad account name",
                        "account_key": "bad account key",
                        "container_name": "bad container name"}
        self.secrets = fake_secrets