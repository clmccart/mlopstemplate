from abc import ABC, abstractmethod

class iSecret(ABC):
    defaults_secrets = "default secrets"
    def __init__(self):
        pass
    
    @abstractmethod
    def set_up_secrets(self):
        self.secrets = default_secrets
    

   