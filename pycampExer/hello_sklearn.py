"""
Hello Scikit learn
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

"""DataFormat
data 2dim = (num_sample,num_features)
label is supported to be 1-dimensional
"""

"""
instance model 
use fit to learn
predict to predict
"""

"""DataTransformation
instance model
fit to train
transform data
"""

"""
You can fit large dataset batch process with `partial_fit`
"""


def main():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

    classifier = MLPClassifier(max_iter=1000)
    classifier.fit(X_train, y_train)
    s = classifier.score(X_test, y_test)
    print(s)


if __name__ == '__main__':
    main()
