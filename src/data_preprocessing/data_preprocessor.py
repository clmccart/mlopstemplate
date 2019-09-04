class DataPreprocessor:
    def __init__(self, df, steps=[]):
        self.df = df
        self.steps = steps
    
    def get_df(self):
        return self.df

    def preprocess(self):
        for step in self.steps:
            self.df = step.run_step(self.df)
        return self.df

    def remove_rows_based_on_value(self, column_name, bad_values):
        for bad_value in bad_values:
            self.df = self.df[self.df[column_name] != bad_value]
        self.df = self.df.reset_index(drop=True)
        return self.df

