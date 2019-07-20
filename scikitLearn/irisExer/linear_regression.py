import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron


def main():
    iris = load_iris()
    X = iris.data[:, (2, 3)]  # 花弁の長さ、花弁の幅
    y = (iris.target == 0.).astype(np.int32)
    perceptron_classifier = Perceptron(random_state=42)
    perceptron_classifier.fit(X, y)
    y_prediction = perceptron_classifier.predict([[2, 0.5]])
    print(y_prediction)


if __name__ == '__main__':
    main()
