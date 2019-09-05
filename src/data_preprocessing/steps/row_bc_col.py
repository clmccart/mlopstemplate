from src.data_preprocessing.steps.istep import iStep

class RemoveRowBcColStep(iStep):

    def __init__(self, column_name, bad_values=[]):
        super().__init__()
        self.column_name = column_name
        self.bad_values = bad_values

    def run_step(self, df):
        for bad_value in self.bad_values:
            df = df[df[self.column_name] != bad_value]
        df = df.reset_index(drop=True)
        return df

