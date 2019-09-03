from src.data_ingestion.iservice import iService
import pandas as pd

class FakeService(iService):

    def get_df(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
        df = pd.DataFrame(data)
        return df