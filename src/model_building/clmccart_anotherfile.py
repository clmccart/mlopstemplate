from sklearn import svm
from sklearn import datasets
import pickle

clf = svm.SVC(gamma='scale')

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf.fit(X, y)

pickle.dump(clf, open("model2.pkl", "wb"))
