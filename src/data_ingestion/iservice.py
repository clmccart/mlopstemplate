from abc import ABC, abstractmethod

class iService(ABC):
    def __init__(self, desired_file=None, ):
        if desired_file == None:
            throw Exception("desired_file is None. You must pass a file for retrieval.")
        pass
    
    @abstractmethod
    def get_df(self):
        return