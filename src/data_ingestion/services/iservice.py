from abc import ABC, abstractmethod

class iService(ABC):

    def __init__(self, desired_file=None, secret_provider=None):
        if desired_file == None:
            raise Exception("desired_file is None. You must specify a file for retrieval.")
        if secret_provider == None:
            raise Exception("secret_provider is None. You must specify the service you are using for secret handling.")
        self.desired_file = desired_file
        self.secret_provider = secret_provider()
        self.secret_provider.set_up_secrets()
    
    @abstractmethod
    def get_df(self):
        return

    def connect_to_service(self):
        pass
    
    def locate_desired_file(self):
        pass
    
    def download_file_as_df(self):
        pass