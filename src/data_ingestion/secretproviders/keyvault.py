from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials
from src.data_ingestion.secretproviders.isecret import iSecret
import os

class KeyVaultProvider(iSecret):

    def __init__(self):
        super().__init__()
        self.retrieve_env_variables()    

    def set_up_secrets(self):
        self.setup_clients()
        self.secrets = self.retrieve_secrets()
    
    def retrieve_env_variables(self):
        self.subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

        self.credentials = ServicePrincipalCredentials(
            client_id=os.environ['AZURE_CLIENT_ID'],
            secret=os.environ['AZURE_CLIENT_SECRET'],
            tenant=os.environ['AZURE_TENANT_ID']
        )
    
    def setup_clients(self):
        self.client = KeyVaultClient(credentials)

    def retrieve_secrets(self):
        # VAULT_URL must be in the format 'https://<vaultname>.vault.azure.net'
        # SECRET_VERSION is required, and can be obtained with the KeyVaultClient.get_secret_versions(self, vault_url, secret_id) API
        secrets_bundle = client.get_secrets(VAULT_URL, SECRET_ID, SECRET_VERSION)
        secrets = self.convert_bundle_to_json(secrets_bundle)
        return secrets
    
    def convert_bundle_to_json(self, secrets_bundle):
        for secret in secrets_bundle:
            print("secret id: ")
            print(secret.id)
            print("secret tags: ")
            print(secret.tags)
        return secrets
