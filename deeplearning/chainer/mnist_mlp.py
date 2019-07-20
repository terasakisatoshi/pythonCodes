"""
reference
http://qiita.com/_329_/items/bcc306194d52f7b81b5a
"""

from sklearn.datasets import fetch_mldata
from sklearn.cross_validation import train_test_split
import numpy as np

import chainer
from chainer import functions as F
from chainer import links as L
from chainer import optimizers


class MnistModel(chainer.Chain):
    def __init__(self):
        super(MnistModel, self).__init__(
            l1=L.Linear(784, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 10)
        )

    def __call__(self, x, t, train):
        x = chainer.Variable(x)
        t = chainer.Variable(t)

        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        h = self.l3(h)

        if train:
            return F.softmax_cross_entropy(h, t), F.accuracy(h, t)
        else:
            return F.accuracy(h, t)


def main():
    mnist = fetch_mldata('MNIST original', data_home=".")
    mnist.data = mnist.data.astype(np.float32)*1.0/255.0
    mnist.target = mnist.target.astype(np.int32)

    train_data, test_data, train_label, test_label = train_test_split(
        mnist.data, mnist.target, test_size=10000, random_state=222)

    print("data shape", mnist.data.dtype, mnist.data.shape)
    print("label shape", mnist.target.dtype, mnist.target.shape)

    model = MnistModel()
    optimizer = optimizers.Adam()
    optimizer.setup(model)

    for each in range(100):
        model.zerograds()
        loss, acc = model(train_data, train_label, train=True)
        loss.backward()
        optimizer.update()
        print("acc", acc.data)

    acc = model(test_data, test_label, train=False)
    print("acc test", acc.data)


if __name__ == '__main__':
    main()
