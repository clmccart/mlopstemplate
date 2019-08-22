class DataPreprocessor:
    def __init__(self, df):
        self.df = df
    
    def donothing(self):
        return self.df

    ''''Example of a preprocessing step function
        and how it fits into the workflow.
        Takes in a dataframe and returns a modified
        dataframe.
        This example drops a column.
    '''
    def step1(self, column_name):
        self.df = self.df.drop(columns=[column_name])
        return self.df