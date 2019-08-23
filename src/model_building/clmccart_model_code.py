import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.data_preprocessing.data_preprocessor import DataPreprocessor
from helpers.data_ingestion.data_ingestion import DataIngestor

from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC(gamma='scale')

ingestor = DataIngestor('iris.csv', 'secrets.json')
df = ingestor.get_df()
dp = DataPreprocessor(df)
dp.drop_columns(['sepal_length'])
dp.remove_rows_based_on_value(column_name='sepal_width', 
                            bad_values=[3.5])
df = dp.get_df()

y = df['species']
X = df.drop(columns=['species'])

clf.fit(X, y)

pickle.dump(clf, open("model.pkl", "wb"))
