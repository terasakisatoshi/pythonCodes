import logging

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.python.framework.ops import Tensor
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def func(x, w0, w1):
    if isinstance(x, Tensor):
        cos = tf.math.cos
        sin = tf.math.sin
        exp = tf.math.exp
    else:
        sin = np.sin
        cos = np.cos
        exp = np.exp
    return w0 * x + w1 * x * x * x


def data_func(x, w0, w1):
    y = func(x, w0, w1)
    y = np.sin(x)
    return y


def get_dataset(w0, w1, sigma=0.1):
    xs = np.random.choice(np.linspace(-np.pi, np.pi, 100), 20)
    ys = data_func(xs, w0, w1) + sigma * np.random.randn(len(xs))
    return xs.astype(np.float32), ys.astype(np.float32)


def main():
    a = -1 / 6  # truth w1
    b = 1  # truth w0
    randrange = 2
    init_w1 = np.random.choice(np.arange(a - randrange, a + randrange, 0.1))
    init_w0 = np.random.choice(np.arange(b - randrange, b + randrange, 0.1))
    #init_w1 = a
    #init_w0 = b
    logger.info("{} {}".format(init_w0, init_w1))
    x = tf.placeholder(dtype=tf.float32, shape=(None,), name="x")
    w0 = tf.Variable(initial_value=init_w0, dtype=tf.float32, name="w0")
    w1 = tf.Variable(initial_value=init_w1, dtype=tf.float32, name="w1")
    # define linear model
    y = func(x, w0, w1)

    # prepare train set
    x_train, y_train = get_dataset(w0=b, w1=a)

    loss1 = tf.nn.l2_loss(y - y_train, name="loss")
    lam = 0.1
    # lam = 0
    loss2 = lam * (w0 * w0 + w1 * w1)
    loss = loss1 + loss2
    opt = tf.train.GradientDescentOptimizer(learning_rate=0.0005)
    minimizer = opt.minimize(loss)

    ws0 = []
    ws1 = []
    losses = []
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        init_w0, init_w1 = sess.run([w0, w1])
        for trial in range(1000):
            current_w0, current_w1, current_loss, _ = sess.run([w0, w1, loss, minimizer],
                                                               feed_dict={x: x_train})
            if trial % 100 == 0:
                ws0.append(current_w0)
                ws1.append(current_w1)
                losses.append(current_loss)
                logger.info("loss {}".format(current_loss))
                logger.info("w0 {}, w1 {}".format(current_w0, current_w1))

    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    plotrange = randrange * 1
    W0, W1 = np.meshgrid(np.arange(b - plotrange, b + plotrange, 0.1),
                         np.arange(a - plotrange, a + plotrange, 0.1))
    F = np.zeros((*W0.shape, len(x_train)))
    for i, w0 in np.ndenumerate(W0):
        F[i] = (y_train - func(x_train, W0[i], W1[i]))**2 + lam * (W0[i] * W0[i] + W1[i] * W1[i])
    F = np.sum(F, axis=-1) / 2
    losses = np.array(losses)
    print(F.shape)
    cont = ax1.contour(W0, W1, F,
                       levels=np.linspace(np.min(losses), np.max(losses), 10),
                       colors=['black'])
    cont.clabel(fmt='%1.1f', fontsize=14)
    #plotrange = randrange * 2
    # contf = ax1.contourf(np.arange(b - randrange, b + randrange, 0.1),
    #                     np.arange(a - randrange, a + randrange, 0.1),
    #                     F)
    ax1.scatter(b, a, c='k', label='ground truth')
    ax1.scatter(init_w0, init_w1, c='red', label='begin')
    ax1.scatter(ws0, ws1, c='b')
    ax1.scatter(ws0[-1], ws1[-1], c='g', label='end')
    ax1.legend()
    ax2.plot(x_train, y_train, '*b', label='ground truth')
    ax2.plot(x_train, func(x=x_train, w0=ws0[-1], w1=ws1[-1]), '+r', label='prediction')
    ax2.legend()
    logger.info(np.sum((y_train - func(x_train, ws0[0], ws1[0]))**2) / 2)
    logger.info(np.sum((y_train - func(x_train, b, a))**2) / 2)
    logger.info(np.sum((y_train - func(x_train, ws0[-1], ws1[-1]))**2) / 2)
    plt.show()


if __name__ == '__main__':
    main()
