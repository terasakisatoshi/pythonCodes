import argparse

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training, datasets, iterators, optimizers
from chainer.training import extensions
import numpy as np
from tqdm import tqdm

major, _, _ = chainer.__version__.split(".")
MAJOR = int(major)
if MAJOR >= 5:
    from chainer import static_graph
else:
    def static_graph(func):
        """
        dummy decorator to keep compatibility between Chainer v5 and v4
        """

        def wrap(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        return wrap

DEVICE = 0
BATCH_SIZE = 32


class MNISTCONV(chainer.Chain):

    def __init__(self, use_static):
        super(MNISTCONV, self).__init__()
        ksize = 3
        hidden_ch = 8
        self.use_static = use_static
        with self.init_scope():
            self.c1 = L.Convolution2D(1, hidden_ch, ksize=ksize, stride=1, pad=ksize // 2)
            self.c2 = L.Convolution2D(hidden_ch, hidden_ch, ksize=ksize, stride=1, pad=ksize // 2)
            self.c3 = L.Convolution2D(hidden_ch, hidden_ch, ksize=ksize, stride=1, pad=ksize // 2)
            linear_size = 28 // 2
            self.l1 = L.Linear(linear_size * linear_size * hidden_ch, 10)

    def _forward(self, x):
        h = self.c1(x)
        h = self.c2(h)
        h = self.c3(h)
        h = F.relu(h)
        h = F.max_pooling_2d(h, 2)
        h = self.l1(h)
        return h

    @chainer.static_graph
    def static_forward(self, x):
        return self._forward(x)

    def forward(self, x):
        if self.use_static and chainer.backends.cuda.get_array_module(x) != np:
            return self.static_forward(x)
        else:
            return self._forward(x)

    def __call__(self, x, t=None, train=True):
        h = self.forward(x)
        if train:
            loss = F.softmax_cross_entropy(h, t)
            chainer.reporter.report({
                'loss': loss,
            }, self)
            return loss
        else:
            return F.softmax(h)


def train(model):
    if DEVICE >= 0:
        chainer.cuda.get_device_from_id(DEVICE).use()
        chainer.cuda.check_cuda_available()
        model.to_gpu()
    train, test = chainer.datasets.get_mnist(ndim=3)
    train_iter = iterators.SerialIterator(train, BATCH_SIZE, shuffle=True)
    test_iter = iterators.SerialIterator(test, BATCH_SIZE, repeat=False, shuffle=False)

    optimizer = optimizers.SGD()
    optimizer.setup(model)

    updater = training.StandardUpdater(train_iter, optimizer, device=DEVICE)
    trainer = training.Trainer(updater, (5, 'epoch'), out='result')
    trainer.extend(extensions.Evaluator(test_iter, model, device=DEVICE))
    trainer.extend(extensions.ProgressBar())
    trainer.extend(extensions.LogReport())
    trainer.extend(extensions.PrintReport([
        'epoch', 'elapsed_time',
        'main/loss', 'validation/main/loss',
    ]))
    trainer.run()

    chainer.serializers.save_npz('result/mnistconv.npz', model)


def predict(model, use_ideep):
    chainer.serializers.load_npz('result/mnistconv.npz', model)
    train, test = chainer.datasets.get_mnist(ndim=3)
    counter = 0
    acc = 0
    if use_ideep and chainer.backends.intel64.is_ideep_available():
        model.to_intel64()
    with chainer.using_config('use_ideep', 'auto'):
        for t in tqdm(test):
            counter += 1
            x, ans = t
            result = model(np.array([x]), train=False).data[0]
            if ans == np.argmax(result):
                acc += 1
        print(acc / counter)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--static', action='store_true', help='decorate static_graph on training')
    parser.add_argument('--ideep', action='store_true', help='use ideep on prediction')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    klass = MNISTCONV
    use_static = args.static
    use_ideep = args.ideep

    model = klass(use_static)
    train(model)
    # initialize
    model = klass(use_static)
    predict(model, use_ideep)


if __name__ == '__main__':
    main()
