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


