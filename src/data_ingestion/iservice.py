from abc import ABC, abstractmethod

class iService(ABC):

    def __init__(self, desired_file=None, secrets=None):
        if desired_file == None:
            raise Exception("desired_file is None. You must specify a file for retrieval.")
        if secrets == None:
            raise Exception("secret_provider is None. You must specify the service you are using for secret handling.")
        self.desired_file = desired_file
        self.secrets = secrets()
        self.secrets.set_up_secrets()
    
    @abstractmethod
    def get_df(self):
        return