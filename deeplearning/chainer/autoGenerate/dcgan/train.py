import chainer
from dcgan_net import Generator, Discriminator, IMAGE_SIZE
import os
from PIL import Image
from chainer import training, iterators, optimizers
from chainer.training import extensions
from custom_updater import Updater
import numpy as np
BATCH_SIZE = 10
DEVICE = 1
RESUME=False
def train():
    model_gen = Generator()
    model_dis = Discriminator()

    if DEVICE >= 0:
        chainer.cuda.get_device_from_id(DEVICE).use()
        chainer.cuda.check_cuda_available()
        model_gen.to_gpu(DEVICE)
        model_dis.to_gpu(DEVICE)

    images = []

    fs = os.listdir('train')
    for f in fs:
        img = Image.open(
            'train/'+f).convert('RGB').resize((IMAGE_SIZE, IMAGE_SIZE))
        hpix = np.array(img, dtype=np.float32)/255.0
        hpix = hpix.transpose(2, 0, 1)
        images.append(hpix)

    train_iter = iterators.SerialIterator(images, BATCH_SIZE, shuffle=True)

    optimizer_gen = optimizers.Adam(alpha=0.0002, beta1=0.5)
    optimizer_gen.setup(model_gen)
    optimizers_dis = optimizers.Adam(alpha=0.0002, beta1=0.5)
    optimizers_dis.setup(model_dis)

    updater = Updater(
        train_iter, {'opt_gen': optimizer_gen, 'opt_dis': optimizers_dis}, device=DEVICE)

    trainer = training.Trainer(updater, (100000, 'epoch'), out='result')
    trainer.extend(extensions.ProgressBar())

    snapshot_interval = (5000, 'epoch')
    trainer.extend(extensions.snapshot(
        filename='snapshot_epoch_{.updater.epoch}.npz'),
        trigger=snapshot_interval)
    trainer.extend(extensions.snapshot_object(
        model_gen, 'model_gen_epoch_{.updater.epoch}.npz'), trigger=snapshot_interval)
    trainer.extend(extensions.snapshot_object(
        model_dis, 'model_dis_epoch_{.updater.epoch}.npz'), trigger=snapshot_interval)
    if RESUME:
        chainer.serializers.load_npz('result/snapshot_epoch_26797.npz',trainer)
    trainer.run()


def main():
    train()


if __name__ == '__main__':
    main()
