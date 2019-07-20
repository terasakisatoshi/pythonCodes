import itertools

import numpy as np
from matplotlib import pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(cnf_mat, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues):
    if normalize:
        cnf_mat = cnf_mat.astype("float") / cnf_mat.sum(axis=1)[:, np.newaxis]
    plt.imshow(cnf_mat, interpolation="nearest", cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = ".2f" if normalize else "d"
    thresh = cnf_mat.max() / 2
    for i, j in itertools.product(range(cnf_mat.shape[0]), range(cnf_mat.shape[1])):
        plt.text(j, i, format(cnf_mat[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cnf_mat[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")


def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    class_names = iris.target_names
    print("ClassNames", class_names)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    classifier = svm.SVC(kernel="linear", C=0.01)
    y_pred = classifier.fit(X_train, y_train).predict(X_test)
    cnf_matrix = confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    plot_confusion_matrix(cnf_matrix, classes=class_names)
    plt.show()


if __name__ == '__main__':
    main()
