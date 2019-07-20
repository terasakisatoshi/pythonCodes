import os 
import numpy as np
import chainer
from chainer import Chain, Variable
from mnist_cnn import CnnModel

def predict(img):
    print("lets predict")
    model=CnnModel()
    chainer.serializers.load_npz(os.path.join('result','cnn_10.npz'),model)
    model.to_cpu()
    x=Variable(np.array([[img]]))
    result = np.argmax(model.fwd(x).data)
    print('result',result)