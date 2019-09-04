from src.data_preprocessing.steps.istep import iStep

class DropColumnsStep(iStep):

    def __init__(self, column_names=[]):
        super().__init__()
        self.column_names = column_names

    def run_step(self, df):
        df = df.drop(columns=self.column_names)
        return df

