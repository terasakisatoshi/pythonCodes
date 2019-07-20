import chainer
import chainer.links as L
import chainer.functions as F

IMAGE_SIZE = 128
NEURON_SIZE = 64
IN_CH = 3


class Generator(chainer.Chain):
    def __init__(self):
        w = chainer.initializers.Normal(scale=0.02, dtype=None)
        super(Generator, self).__init__()
        with self.init_scope():
            self.l0 = L.Linear(100, NEURON_SIZE * IMAGE_SIZE * IMAGE_SIZE // 8 // 8,
                               initialW=w)
            self.dc1 = L.Deconvolution2D(
                NEURON_SIZE, NEURON_SIZE // 2, 4, 2, 1, initialW=w)
            self.dc2 = L.Deconvolution2D(
                NEURON_SIZE // 2, NEURON_SIZE // 4, 4, 2, 1, initialW=w)
            self.dc3 = L.Deconvolution2D(
                NEURON_SIZE // 4, NEURON_SIZE // 8, 4, 2, 1, initialW=w)
            self.dc4 = L.Deconvolution2D(
                NEURON_SIZE // 8, 3, 3, 1, 1, initialW=w)
            self.bn0 = L.BatchNormalization(
                NEURON_SIZE * IMAGE_SIZE * IMAGE_SIZE // 8 // 8)
            self.bn1 = L.BatchNormalization(NEURON_SIZE // 2)
            self.bn2 = L.BatchNormalization(NEURON_SIZE // 4)
            self.bn3 = L.BatchNormalization(NEURON_SIZE // 8)

    def __call__(self, z):
        shape = (len(z), NEURON_SIZE, IMAGE_SIZE // 8, IMAGE_SIZE // 8)
        h = F.reshape(F.relu(self.bn0(self.l0(z))), shape)
        h = F.relu(self.bn1(self.dc1(h)))
        h = F.relu(self.bn2(self.dc2(h)))
        h = F.relu(self.bn3(self.dc3(h)))
        x = F.sigmoid(self.dc4(h))
        return x


class Discriminator(chainer.Chain):
    def __init__(self):
        w = chainer.initializers.Normal(scale=0.02, dtype=None)
        super(Discriminator, self).__init__()
        with self.init_scope():
            self.c0_0 = L.Convolution2D(
                3, NEURON_SIZE // 8, 3, 1, 1, initialW=w)
            self.c0_1 = L.Convolution2D(
                NEURON_SIZE // 8, NEURON_SIZE // 4, 4, 2, 1, initialW=w)
            self.c1_0 = L.Convolution2D(
                NEURON_SIZE // 4, NEURON_SIZE // 4, 3, 1, 1, initialW=w)
            self.c1_1 = L.Convolution2D(
                NEURON_SIZE // 4, NEURON_SIZE // 2, 4, 2, 1, initialW=w)
            self.c2_0 = L.Convolution2D(
                NEURON_SIZE // 2, NEURON_SIZE // 2, 3, 1, 1, initialW=w)
            self.c2_1 = L.Convolution2D(
                NEURON_SIZE // 2, NEURON_SIZE, 4, 2, 1, initialW=w)
            self.c3_0 = L.Convolution2D(
                NEURON_SIZE, NEURON_SIZE, 3, 1, 1, initialW=w)
            self.l4 = L.Linear(NEURON_SIZE * IMAGE_SIZE *
                               IMAGE_SIZE // 8 // 8, 1, initialW=w)
            self.bn0_1 = L.BatchNormalization(
                NEURON_SIZE // 4, use_gamma=False)
            self.bn1_0 = L.BatchNormalization(
                NEURON_SIZE // 4, use_gamma=False)
            self.bn1_1 = L.BatchNormalization(
                NEURON_SIZE // 2, use_gamma=False)
            self.bn2_0 = L.BatchNormalization(
                NEURON_SIZE // 2, use_gamma=False)
            self.bn2_1 = L.BatchNormalization(NEURON_SIZE, use_gamma=False)
            self.bn3_0 = L.BatchNormalization(NEURON_SIZE, use_gamma=False)

    def __call__(self, x):
        h = F.leaky_relu(self.c0_0(x))
        h = F.dropout(F.leaky_relu(self.bn0_1(self.c0_1(h))), ratio=0.2)
        h = F.dropout(F.leaky_relu(self.bn1_0(self.c1_0(h))), ratio=0.2)
        h = F.dropout(F.leaky_relu(self.bn1_1(self.c1_1(h))), ratio=0.2)
        h = F.dropout(F.leaky_relu(self.bn2_0(self.c2_0(h))), ratio=0.2)
        h = F.dropout(F.leaky_relu(self.bn2_1(self.c2_1(h))), ratio=0.2)
        h = F.dropout(F.leaky_relu(self.bn3_0(self.c3_0(h))), ratio=0.2)
        return self.l4(h)
