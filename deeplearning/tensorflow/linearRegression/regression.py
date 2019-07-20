from collections import defaultdict
import os

import numpy as np
import tensorflow as tf


def linear_model(x, freeze_vars=[]):
    trainable = defaultdict(lambda: True)
    for v in freeze_vars:
        trainable[v] = False
    with tf.variable_scope("linear", reuse=tf.AUTO_REUSE):
        a = tf.Variable(initial_value=1.0, dtype=tf.float32, name="a", trainable=trainable["a"])
        b = tf.Variable(initial_value=0.0, dtype=tf.float32, name="b", trainable=trainable["b"])
        return a, b, a * x + b


def train():
    x_train = np.linspace(0, np.pi, 50)
    a = -1.0
    b = 3.0
    mu = 0
    sigma = 0.2
    y_train = a * x_train + b + sigma * np.random.randn() + mu

    x = tf.placeholder(dtype=tf.float32, shape=(None,))
    a, b, y = linear_model(x)
    loss = tf.nn.l2_loss(y - y_train, name="loss")
    opt = tf.train.GradientDescentOptimizer(learning_rate=0.005)
    minimizer = opt.minimize(loss)

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for _ in range(300):
            a_train, b_train, current_loss, _ = sess.run([a, b, loss, minimizer], feed_dict={x: x_train})
        if not os.path.exists("checkpoint"):
            os.mkdir("checkpoint")
        saver.save(sess, "checkpoint/model")
    print(a_train, b_train)


def restore_b_only():
    """
    restore only b
    """
    x = tf.placeholder(dtype=tf.float32, shape=(None,))
    _, b, y = linear_model(x)
    # a = tf.get_variable("linear/a", shape=(), initializer=tf.constant_initializer())
    saver = tf.train.Saver({"linear/b": b})
    ckpt_path = tf.train.latest_checkpoint("checkpoint")
    with tf.Session() as sess:
        saver.restore(sess, ckpt_path)
        # a.initializer.run()
        # print(sess.run(a))
        print(sess.run(b))


def restore_a_b():
    x = tf.placeholder(dtype=tf.float32, shape=(None,))
    a, b, y = linear_model(x)
    saver = tf.train.Saver()
    ckpt_path = tf.train.latest_checkpoint("checkpoint")
    with tf.Session() as sess:
        saver.restore(sess, ckpt_path)
        print(sess.run(a))
        print(sess.run(b))


def retrain_a():
    """specify train parameter via var_list"""
    x_train = np.linspace(0, np.pi, 50)
    a = 2
    b = 3.5
    mu = 0
    sigma = 0.2
    y_train = a * x_train + b + sigma * np.random.randn() + mu

    x = tf.placeholder(dtype=tf.float32, shape=(None,))
    a, b, y = linear_model(x)
    loss = tf.nn.l2_loss(y - y_train, name="loss")
    opt = tf.train.GradientDescentOptimizer(learning_rate=0.005)
    minimizer = opt.minimize(loss, var_list=[a])

    saver = tf.train.Saver()
    ckpt_path = tf.train.latest_checkpoint("checkpoint")
    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, ckpt_path)
        for _ in range(300):
            a_train, b_train, current_loss, _ = sess.run([a, b, loss, minimizer], feed_dict={x: x_train})
            print(a_train, b_train, current_loss)


def retrain_b():
    x_train = np.linspace(0, np.pi, 50)
    a = 2
    b = 3.5
    mu = 0
    sigma = 0.2
    y_train = a * x_train + b + sigma * np.random.randn() + mu

    x = tf.placeholder(dtype=tf.float32, shape=(None,))
    a, b, y = linear_model(x, freeze_vars=["a"])
    loss = tf.nn.l2_loss(y - y_train, name="loss")
    opt = tf.train.GradientDescentOptimizer(learning_rate=0.005)

    minimizer = opt.minimize(loss)

    saver = tf.train.Saver()
    ckpt_path = tf.train.latest_checkpoint("checkpoint")
    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, ckpt_path)
        for _ in range(300):
            a_train, b_train, current_loss, _ = sess.run([a, b, loss, minimizer], feed_dict={x: x_train})
            print(a_train, b_train, current_loss)


def main():
    train()
    tf.reset_default_graph()
    retrain_b()


if __name__ == '__main__':
    main()
