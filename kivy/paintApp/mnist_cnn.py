import os 
import numpy as np
import chainer
from chainer import datasets
from chainer import Chain, Variable
from chainer import iterators, optimizers, training
from chainer.training import extensions

import chainer.functions as F 
import chainer.links as L 

class CnnModel(Chain):
    def __init__(self):
        super(CnnModel,self).__init__(
            cn1=L.Convolution2D(1,20,5),
            cn2=L.Convolution2D(20,50,5),
            fc1=L.Linear(800,500),
            fc2=L.Linear(500,10),
        )

    def __call__(self,x,t):
        return F.softmax_cross_entropy(self.fwd(x),t)

    def fwd(self,x):
        h1=F.max_pooling_2d(F.relu(self.cn1(x)),2)
        h2=F.max_pooling_2d(F.relu(self.cn2(h1)),2)
        h3=F.dropout(F.relu(self.fc1(h2)))
        return self.fc2(h3)

def train(num_loop):
    chainer.cuda.get_device_from_id(0).use()
    model=CnnModel()
    model.to_gpu()

    optimizer=optimizers.Adam()
    optimizer.setup(model)
    minibatch_size=1000
    train, test = datasets.get_mnist(ndim=3)
    iterator = iterators.SerialIterator(train, minibatch_size)
    updater=training.StandardUpdater(iterator,optimizer,device=0)
    loops=(num_loop,'epoch')
    if not os.path.exists('result'):
        os.mkdir('result')
    trainer = training.Trainer(updater,loops,out='result')
    trainer.extend(extensions.ProgressBar())
    trainer.extend(extensions.snapshot_object(
        model, 'cnn_{.updater.epoch}.npz'), trigger=(1,'epoch'))
    print('start to train')
    trainer.run()
    print('finish to train')


def check_accuracy(num_loop):
    print("lets check_accuracy")
    train, test = datasets.get_mnist(ndim=3)
    model=CnnModel()
    chainer.serializers.load_npz(os.path.join('result','cnn_{}.npz'.format(num_loop)),model)
    model.to_cpu()
    counter=0
    for t in test:
        img,label=t
        x=Variable(np.array([img]))
        predict = np.argmax(model.fwd(x).data)
        if predict==label:
            counter+=1
    print("done")
    print(counter/len(test))


def main():
    num_loop=10
    train(num_loop)
    check_accuracy(num_loop)
if __name__ == '__main__':
    main()