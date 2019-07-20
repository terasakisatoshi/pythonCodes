from dcgan_net import Generator
import chainer
import numpy as np
import codecs
from PIL import Image
DEVICE = 0
xp = chainer.cuda.cupy if DEVICE>=0 else np


def generate():
    import os 
    if not os.path.exists('output'):
        os.mkdir('output')

    generator = Generator()

    if DEVICE >= 0:
        chainer.cuda.get_device_from_id(DEVICE).use()
        chainer.cuda.check_cuda_available()
        generator.to_gpu(DEVICE)

    chainer.serializers.load_npz('result/model_gen_epoch_10000.npz', generator)
    num_generate = 100
    rnd = np.random.uniform(-1, 1, (num_generate, 100, 1, 1))
    rnd = xp.array(rnd, dtype=xp.float32)
    with chainer.using_config('train',False):
        result=generator(rnd)

    f=codecs.open('vectors.txt','w','utf8')
    for i in range(num_generate):
        data=np.zeros((128,128,3),dtype=np.uint8)
        if DEVICE>=0:
            dst=result.data[i].get()*255.0
        else:
            dst=result.data[i]*255.0
        data[:,:,0]=dst[0]
        data[:,:,1]=dst[1]
        data[:,:,2]=dst[2]
        himg=Image.fromarray(data,'RGB')
        himg.save('output/gen_{}.png'.format(i))
        f.write(','.join([str(j) for j in rnd[i][:,0][:,0]]))
        f.write('\n')
    f.close()

def main():
    generate()


if __name__ == '__main__':
    main()
