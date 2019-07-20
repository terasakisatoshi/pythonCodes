from chainer import datasets
from chainer import Chain, Variable
from chainer import iterators, optimizers, training
from chainer.training import extensions
import numpy as np
import chainer.functions as F
import chainer.links as L


def show_dataset():
    from matplotlib import pyplot as plt
    train, test = datasets.get_mnist(ndim=3)
    for t in train[:10]:
        img, label = t
        img = (255*img.reshape(img.shape[1:])).astype(np.uint8)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(str(label))
        plt.show()


class MnistModel(Chain):

    def __init__(self):
        super(MnistModel, self).__init__(
            l1=L.Linear(28**2, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 10)
        )

    def __call__(self, x, t):
        return F.softmax_cross_entropy(self.fwd(x), t)

    def fwd(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)


def main():
    # get mnist dataset as TupleDataset
    train, test = datasets.get_mnist(ndim=3)
    model = MnistModel()
    optimizer = optimizers.Adam()
    optimizer.setup(model)
    minibatch_size = 1000
    iterator = iterators.SerialIterator(train, minibatch_size)
    updater = training.StandardUpdater(iterator, optimizer)
    loops = (10, 'epoch')
    trainer = training.Trainer(updater, loops)
    trainer.extend(extensions.ProgressBar())
    trainer.run()

    counter = 0

    for t in test:
        img, label = t
        x = Variable(img)
        predict = np.argmax(model.fwd(x).data)
        if predict == label:
            counter += 1

    print(counter/len(test))
if __name__ == '__main__':
    main()
