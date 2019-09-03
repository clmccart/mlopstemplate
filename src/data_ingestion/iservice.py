from abc import ABC, abstractmethod

class iService(ABC):

    def __init__(self, desired_file=None, service=None, secrets=None):
        if desired_file == None:
            raise Exception("desired_file is None. You must specify a file for retrieval.")
        if service == None:
            raise Exception("service is None. You must specify what service you would like to pull the data from.")
        if secrets == None:
            raise Exception("secrets is None. You must specify the service you are using for secret handling.")
        self.desired_file = desired_file
        self.service = service
        self.secrets = secrets
        self.secrets.set_up_secrets()
    
    @abstractmethod
    def get_df(self):
        return