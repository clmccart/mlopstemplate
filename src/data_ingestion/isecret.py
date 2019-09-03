from abc import ABC, abstractmethod

class iSecret(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def setup_secrets(self):
        pass