from abc import ABC, abstractmethod

class iStep(ABC):

    def __init__(self, df, column_names):
        super().__init__(df, column_names)
        self.df = df
        self.column_names = column_names
    
    @abstractmethod
    def run_step(self):
        self.df = self.df.drop(columns=self.column_names)
        return self.df
