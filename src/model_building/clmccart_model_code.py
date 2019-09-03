import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_preprocessing.data_preprocessor import DataPreprocessor
from src.data_ingestion.data_ingestion import DataIngestor
from src.data_ingestion.blob_service import BlobService
from src.data_ingestion.secret_json_handler import SecretJSON

from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC(gamma='scale')
secret_provider = SecretJSON()
ingestor = DataIngestor(desired_file='iris.csv', 
                        secret_provider=secret_provider, 
                        service=BlobService)
df = ingestor.get_df()
print(df.head())
print("Data has been ingested")
# dp = DataPreprocessor(df)
# dp.drop_columns(['sepal_length'])
# dp.remove_rows_based_on_value(column_name='sepal_width', 
#                             bad_values=[3.5])
# df = dp.get_df()

# y = df['species']
# X = df.drop(columns=['species'])

# clf.fit(X, y)
 
# pickle.dump(clf, open("model.pkl", "wb"))
# print("pickle dumped") 
