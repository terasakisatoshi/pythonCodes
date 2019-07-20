"""
Classify handwritten images its data are from MNIST
main reference
https://github.com/oreilly-japan/deep-learning-from-scratch
"""
__author__ = "SatoshiTerasaki<terasakisatoshi.math@gmai.com"
__date__ = '2017/05/05'


import time
from matplotlib import pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.datasets import fetch_mldata

from numba import jit

# functions


def sigmoid(x):
    return 1/(1+np.exp(-x))


def deriv_sigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))


def softmax(x):
    """
    calc softmax function
    note that np.sum(arr,axis=1,keepdims=True) behaves as follow:
    >>> mat=np.arange(12).reshape(3,4)
    >>> mat
    >>> array([[0,1,2,3],
               [4,5,6,7],
               [8,9,10,11]])
    >>> np.sum(mat,axis=1,keepdims=True)
    >>> array([ 6],
              [22],
              [38])
    """
    exp_x = np.exp(x)
    if exp_x.ndim <= 1:
        return exp_x/np.sum(exp_x, keepdims=True)
    else:
        return exp_x/np.sum(exp_x, axis=1, keepdims=True)


def cross_entropy_error(y, t):
    """
    reference Deep Learning From Scratch
    https://github.com/oreilly-japan/deep-learning-from-scratch
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size


def numerical_gradient(f, x):
    """
    reference Deep Learning From Scratch
    https://github.com/oreilly-japan/deep-learning-from-scratch
    """
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)

        x[idx] = tmp_val  # 値を元に戻す
        it.iternext()

    return grad


# create dataset
def get_mnist_data(data_home=None):
    """
    load data on your directry ~/scikit_learn_data/mldata/
    if data doesn't exist, it downloads the data from site.
    """
    mnist = fetch_mldata('MNIST original')
    return mnist


def divide_mnist_data(mnist):
    """
    load mnist dataset
    input:None
    output:split these data into train valid and test data.
    """

    mnist_X, mnist_y = shuffle(mnist.data, mnist.target, random_state=42)
    # normalize
    mnist_X = mnist_X/255.0
    train_X, test_X, train_y, test_y = train_test_split(mnist_X, mnist_y,
                                                        test_size=0.2,
                                                        random_state=42)
    # choose valid data from <test_size> % of train set
    train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y,
                                                          test_size=0.2,
                                                          random_state=42)

    return train_X, valid_X, test_X, train_y, valid_y, test_y


class MultiPerceptron(object):

    def __init__(self, in_size=28*28, hidden_size=100, out_size=10):
        self.parameters = {}
        # Layer1 weights
        W1 = np.random.uniform(low=-0.08, high=0.08,
                               size=(in_size, hidden_size)).astype('float32')
        b1 = np.zeros(hidden_size).astype('float32')
        # Layer2 weights
        W2 = np.random.uniform(low=-0.08, high=0.08,
                               size=(hidden_size, out_size)).astype('float32')
        b2 = np.zeros(out_size).astype('float32')

        for key, value in locals().items():
            self.parameters[key] = value

    def check_parameters(self):
        for key, value in self.parameters.items():
            print('key=', key)
            print('value=', value)

    def __call__(self, xs=None):
        if xs == None:
            self.check_parameters()
        else:
            ys = self.predict(xs)
            return ys

    def predict(self, xs):
        W1, W2 = self.parameters['W1'], self.parameters['W2']
        b1, b2 = self.parameters['b1'], self.parameters['b2']
        z0 = xs
        u1 = np.matmul(z0, W1)+b1
        z1 = sigmoid(u1)
        u2 = np.matmul(z1, W2)+b2
        ys = softmax(u2)
        return ys

    def evaluate(self, xs, ts):
        ys = self.predict(xs)
        labels = np.argmax(ys, axis=1)
        ts = np.argmax(ts, axis=1)
        return np.sum(labels == ts)/float(ys.shape[0])

    def loss(self, xs, ts):
        ys = self.predict(xs)
        return cross_entropy_error(ys, ts)

    def calc_grads_with_naive(self, xs, ts):
        loss_fun = lambda W: self.loss(xs, ts)

        grads = {}
        grads['W1'] = numerical_gradient(loss_fun, self.parameters['W1'])
        grads['b1'] = numerical_gradient(loss_fun, self.parameters['b1'])
        grads['W2'] = numerical_gradient(loss_fun, self.parameters['W2'])
        grads['b2'] = numerical_gradient(loss_fun, self.parameters['b2'])

        return grads

    def back_propagation(self, xs, ts):
        """
        calc back propagation of cross_entropy
        [in] xs: train image data
             ts: one hot vector corresponds the answer of x
        [out]
             pertial derivatives of MSE
        """
        W1, W2 = self.parameters['W1'], self.parameters['W2']
        b1, b2 = self.parameters['b1'], self.parameters['b2']
        grads = {}

        batch_num = xs.shape[0]

        # forward
        z0 = xs
        u1 = np.matmul(z0, W1)+b1
        z1 = sigmoid(u1)
        u2 = np.matmul(z1, W2)+b2
        ys = softmax(u2)
        # backward
        # calc output layer error
        delta_output = (ys - ts) / batch_num
        # backward to hidden layer
        grads['W2'] = np.dot(z1.T, delta_output)
        grads['b2'] = np.sum(delta_output, axis=0)
        # take Hadamard product
        delta_1 = deriv_sigmoid(u1) * np.dot(delta_output, W2.T)
        # backward to hidden layer
        grads['W1'] = np.dot(z0.T, delta_1)
        grads['b1'] = np.sum(delta_1, axis=0)

        return grads


def one_hot_vector(ts):
    label_list = np.identity(10)
    return np.array([label_list[t] for t in list(map(int, ts))])

ITERATIONS = 5000
MINI_BATCH_SIZE = 1000
LEARNING_RATE = 0.1
HIDDEN_SIZE = 100


def main():
    # get data
    print(">>>get mnist data<<<")
    mnist = get_mnist_data()
    train_X, valid_X, test_X, train_y, valid_y, test_y = divide_mnist_data(
        mnist)
    network = MultiPerceptron(hidden_size=HIDDEN_SIZE)

    loss_list = []
    accuracy_list = []
    # start training
    for iteration in range(1, ITERATIONS+1):
        print("----- %d th -----" % iteration)

        started = time.time()

        sampled_indices = np.random.choice(len(train_X), MINI_BATCH_SIZE)
        batch_train_X = train_X[sampled_indices]
        batch_train_y = train_y[sampled_indices]
        batch_train_y = one_hot_vector(batch_train_y)
        grads = network.back_propagation(batch_train_X, batch_train_y)
        # update
        for param in ['W1', 'W2', 'b1', 'b2']:
            network.parameters[param] -= LEARNING_RATE * grads[param]

        end = time.time()

        loss = network.loss(batch_train_X, batch_train_y)
        accuracy = network.evaluate(valid_X, one_hot_vector(valid_y))
        loss_list.append(loss)
        accuracy_list.append(accuracy)
        print('loss', loss)
        print('accuracy', 100*accuracy, '[%]')
        print("elapsed time per iteration ", end-started, " [sec]")

    plt.plot(loss_list)
    plt.plot(accuracy_list)
    plt.show()

if __name__ == '__main__':
    main()
