from abc import ABC, abstractmethod

class iSecret(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def set_up_secrets(self):
        pass
    
    @abstractmethod
    def get_account_name(self):
        return
    
    @abstractmethod
    def get_account_key(self):
        return 
    
    @abstractmethod
    def get_container_name():
        return