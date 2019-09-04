from abc import ABC, abstractmethod

class iSecret(ABC):
    defaults_secrets = {
        "account_name": "",
        "account_key": "",
        "container_name": ""
    }
    def __init__(self):
        pass
    
    '''
    This method must set self.secrets equal to a json with the same format as the default secrets.
    '''
    @abstractmethod
    def set_up_secrets(self):
        self.secrets = default_secrets
    

   