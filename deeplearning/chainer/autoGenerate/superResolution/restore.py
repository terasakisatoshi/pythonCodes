import chainer
import chainer.function as F
import chainer.links as L
from chainer import training, datasets, iterators, optimizers
from chainer.training import extensions
import numpy as np

import math
import sys
from PIL import Image
from PIL import ImageDraw

from train import SuperResolution

DEVICE = 0
PATCH_SIZE=16

if DEVICE >= 0:
    import cupy as xp
    import chainer.cuda
else:
    xp = np


def main():
    model = SuperResolution()
    chainer.serializers.load_hdf5('model.hdf5', model)
    if DEVICE >= 0:
        chainer.cuda.get_device_from_id(DEVICE).use()
        chainer.cuda.check_cuda_available()
        model.to_gpu(DEVICE)

    in_file = 'test.png'
    dest_file = 'dest.png'

    img = Image.open(in_file).convert('YCbCr')

    org_w = w = img.size[0]
    org_h = h = img.size[1]

    #resize img 
    if w % PATCH_SIZE != 0:
        w = (math.floor(w/PATCH_SIZE)+1)*PATCH_SIZE
    if h % PATCH_SIZE != 0:
        h = (main.floor(w/PATCH_SIZE)+1)*PATCH_SIZE
    if w != img.size[0] or h != img.size[1]:
        img = img.resize((w, h))

    dst = Image.new("YCbCr", (10*w//4, 10*h//4), 'white')

    cur_x = 0
    while cur_x <= img.size[0] - PATCH_SIZE:
        cur_y = 0
        while cur_y <= img.size[1]-PATCH_SIZE:
            rect = (cur_x, cur_y, cur_x+PATCH_SIZE, cur_y+PATCH_SIZE)
            cropimg = img.crop(rect)
            hpix = xp.array(cropimg, dtype=xp.float32)
            hpix = hpix[:, :, 0]/255
            x = xp.array([[hpix]], dtype=xp.float32)
            t = model(x, train=False)
            dstimg = cropimg.resize((40, 40), Image.BICUBIC)
            hpix = np.array(dstimg, dtype=xp.float32)
            hpix.flags.writeable = True
            if DEVICE >= 0:
                hpix[:, :, 0] = t.data[0].get()*255
                #hpix[:, :, 0] = chainer.cuda.to_cpu(t.data[0])*255
            else:
                hpix[:, :, 0] = t.data[0]*255
            buf = np.array(hpix.clip(0, 255), dtype=np.uint8)
            himg = Image.fromarray(buf, 'YCbCr')
            dst.paste(himg, (10*cur_x//4, 10*cur_y //
                             4, 10*cur_x//4+40, 10*cur_y//4+40))
            cur_y += PATCH_SIZE
        cur_x += PATCH_SIZE

    dst = dst.convert('RGB')
    dst.save(dest_file)


if __name__ == '__main__':
    main()
