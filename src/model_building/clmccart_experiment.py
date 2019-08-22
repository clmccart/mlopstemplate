import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from helpers.data_ingestion.data_ingestion import DataIngestor

from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC(gamma='scale')

ingestor = DataIngestor('iris.csv', 'secrets.json')
df = ingestor.get_df()

y = df['species']
X = df.drop(columns=['species'])

clf.fit(X, y)

pickle.dump(clf, open("model.pkl", "wb"))
