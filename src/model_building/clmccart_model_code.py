import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_preprocessing.data_preprocessor import DataPreprocessor
from src.data_ingestion.data_ingestion import DataIngestor
from src.data_ingestion.services.blob_service import BlobService
from src.data_ingestion.secretproviders.envvar import EnvVariableProvider
from src.data_preprocessing.steps.drop_columns import DropColumnsStep
from src.data_preprocessing.steps.row_bc_col import RemoveRowBcColStep

from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC(gamma='scale')
secret_provider = EnvVariableProvider
ingestor = DataIngestor(desired_file='iris.csv', 
                        secret_provider=secret_provider, 
                        service=BlobService)
df = ingestor.get_df()
print(df.head())
print("Data has been ingested")
 
steps = [DropColumnsStep('sepal_length'), 
        RemoveRowBcColStep(column_name='sepal_width', bad_values=[3.5])]

dp = DataPreprocessor(df, steps)
df = dp.preprocess()

y = df['species']
X = df.drop(columns=['species'])

clf.fit(X, y)
 
pickle.dump(clf, open("model.pkl", "wb"))
print("pickle dumped") 
