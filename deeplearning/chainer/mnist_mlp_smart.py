"""
reference
http://qiita.com/_329_/items/bcc306194d52f7b81b5a
"""

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training
from chainer.training import extensions
from chainer.training.triggers import MinValueTrigger

import pickle


class MnistModel(chainer.Chain):

    def __init__(self):
        super(MnistModel, self).__init__(
            l1=L.Linear(784, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 10))

    def __call__(self, x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        return self.l3(h)


def save_pkl(filename, obj):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

model = L.Classifier(MnistModel())
optimizer = chainer.optimizers.Adam()
optimizer.setup(model)

train, test = chainer.datasets.get_mnist()
train_iter = chainer.iterators.SerialIterator(train, 100)
test_iter = chainer.iterators.SerialIterator(test, 100, repeat=False, shuffle=False)

updater = training.StandardUpdater(train_iter, optimizer, device=-1)
trainer = training.Trainer(updater, (100, 'epoch'), out="result")
trainer.extend(extensions.Evaluator(test_iter, model, device=-1))
trainer.extend(extensions.LogReport())
trainer.extend(extensions.PrintReport(['epoch', 'main/loss', 'validation/main/loss', 'main/accuracy', 'validation/main/accuracy']))
trainer.extend(extensions.ProgressBar())
trainer.extend(extensions.snapshot_object(model, savefun=save_pkl, filename='model.pkl', trigger=MinValueTrigger(key='validation/main/loss')))

trainer.run()
