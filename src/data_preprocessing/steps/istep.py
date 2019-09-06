from abc import ABC, abstractmethod

class iStep(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def run_step(self, df):
        return df
