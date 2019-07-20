import chainer
from chainer import training
import numpy as np
xp = chainer.cuda.cupy if chainer.cuda.available else np
import chainer.functions as F


class Updater(training.StandardUpdater):

    def __init__(self, train_iter, optimizer, device):
        super(Updater, self).__init__(
            train_iter,
            optimizer,
            device=device)

    def loss_dis(self, dis, y_fake, y_real):
        batchsize = len(y_fake)
        L1 = F.sum(F.softplus(-y_real)) / batchsize
        L2 = F.sum(F.softplus(y_fake)) / batchsize
        loss = L1 + L2
        return loss

    def loss_gen(self, gen, y_fake):
        batchsize = len(y_fake)
        loss = F.sum(F.softplus(-y_fake)) / batchsize
        return loss

    def update_core(self):
        # Iteratorからバッチ分のデータを取得
        batch = self.get_iterator('main').next()
        src = self.converter(batch, self.device)

        # Optimizerを取得
        optimizer_gen = self.get_optimizer('opt_gen')
        optimizer_dis = self.get_optimizer('opt_dis')
        # ニューラルネットワークのモデルを取得
        gen = optimizer_gen.target
        dis = optimizer_dis.target

        # 乱数データを用意
        rnd = np.random.uniform(-1, 1, (src.shape[0], 100))
        rnd = xp.array(rnd, dtype=xp.float32)

        # 画像を生成して認識と教師データから認識
        x_fake = gen(rnd)       # 乱数からの生成結果
        y_fake = dis(x_fake)    # 乱数から生成したものの認識結果
        y_real = dis(src)       # 教師データからの認識結果

        # ニューラルネットワークを学習
        optimizer_dis.update(self.loss_dis, dis, y_fake, y_real)
        optimizer_gen.update(self.loss_gen, gen, y_fake)
