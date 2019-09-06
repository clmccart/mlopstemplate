from src.data_ingestion.secretproviders.isecret import iSecret
import os

class EnvVariableProvider(iSecret):

    def __init__(self):
        pass

    def set_up_secrets(self):
        self.retrieve_env_variables()
        self.retrieve_secrets()   
    
    def retrieve_env_variables(self):
        self.account_name = os.environ['ACCOUNTNAME']
        self.account_key = os.environ['ACCOUNTKEY']
        self.container_name = os.environ['CONTAINERNAME']
    
    def retrieve_secrets(self):
       self.secrets = {
           "account_name" : self.account_name,
           "account_key" : self.account_key,
           "container_name" : self.container_name
       }
       
    