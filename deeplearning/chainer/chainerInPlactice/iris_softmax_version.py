from sklearn import datasets
import numpy as np
import chainer
from chainer import Chain, Variable
from chainer import optimizers
import chainer.links as L
import chainer.functions as F

class IrisChain(Chain):

    def __init__(self):
        super(IrisChain, self).__init__(
            l1=L.Linear(4, 6),
            l2=L.Linear(6, 3)
        )

    def __call__(self, x, y):
        return F.softmax_cross_entropy(self.fwd(x), y)

    def fwd(self, x):
        h1 = F.sigmoid(self.l1(x))
        h2 = self.l2(h1)
        return h2


def create_iris_dataset():
    iris = datasets.load_iris()
    X = iris.data.astype(np.float32)
    Y = iris.target.astype(np.int32)  # Y is composed with three numbers 0,1,2
    N = Y.size

    # split dataset into train and test
    index = np.arange(N)
    odd =index[1:N:2]
    even = index[0:N:2]
    x_train = X[odd]
    y_train = Y[odd]
    x_test = X[even]
    y_test = Y[even]
    return x_train, y_train, x_test, y_test

BATCH, MINI_BATCH, ACCUMLATE = 0, 1, 2
TRAIN_MODE = BATCH


def main():
    x_train, y_train, x_test, y_test = create_iris_dataset()
    # define model
    model = IrisChain()
    optimizer = optimizers.SGD()
    optimizer.setup(model)
    # execute batch-train
    epochs = 10000
    
    if TRAIN_MODE == BATCH:
        for i in range(epochs):
            xs = Variable(x_train)
            ys = Variable(y_train)
            model.cleargrads()
            loss = model(xs, ys)
            loss.backward()
            optimizer.update()

    if TRAIN_MODE == MINI_BATCH:
        n = x_test.shape[0]
        size = n//3
        for e in range(epochs):
            s = np.random.permutation(n)
            for i in range(n//size):
                batch = s[i*size:min((i+1)*size, n)]
                xs = Variable(x_train[batch])
                ys = Variable(y_train[batch])
                model.cleargrads()
                loss = model(xs, ys)
                loss.backward()
                optimizer.update()

    if TRAIN_MODE == ACCUMLATE:
        n = x_test.shape[0]
        size = n//3
        for e in range(epochs):
            accum_loss=None
            s = np.random.permutation(n)
            for i in range(n//size):
                batch = s[i*size:min((i+1)*size, n)]
                xs = Variable(x_train[batch])
                ys = Variable(y_train[batch])
                model.cleargrads()
                loss = model(xs, ys)
                accum_loss=loss if accum_loss is None else accum_loss+loss
            loss.backward()
            optimizer.update()

            # validate
    predict = model.fwd(Variable(x_test)).data
    counter = 0
    for i in range(predict.shape[0]):
        p = np.argmax(predict[i])
        a = y_test[i]
        if p == a:
            counter += 1
    print("accuracy", counter/predict.shape[0])

if __name__ == '__main__':
    main()
