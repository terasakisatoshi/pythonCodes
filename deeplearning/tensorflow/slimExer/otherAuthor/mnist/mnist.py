"""
Exercise for tensorflow.contrib.slim
model Reference:http://arakan-pgm-ai.hatenablog.com/entry/2017/11/23/080000
"""

import tensorflow as tf
import tensorflow.contrib.slim as slim
from tensorflow.examples.tutorials.mnist import input_data
from contextlib import ExitStack


def model(x_image):
    with ExitStack() as stack:
        c1 = stack.enter_context(slim.arg_scope([slim.conv2d, slim.fully_connected],
                                                activation_fn=tf.nn.relu,
                                                weights_initializer=tf.truncated_normal_initializer(
                                                    stddev=0.1),
                                                biases_initializer=tf.constant_initializer(0.1)))
        c2 = stack.enter_context(slim.arg_scope([slim.max_pool2d],
                                                padding="SAME"))
        h_conv1 = slim.conv2d(x_image, 32, [5, 5])
        h_pool1 = slim.max_pool2d(h_conv1, [2, 2])

        h_conv2 = slim.conv2d(h_pool1, 64, [5, 5])
        h_pool2 = slim.max_pool2d(h_conv2, [2, 2])

        h_pool2_flat = slim.flatten(h_pool2)
        h_fc1 = slim.fully_connected(h_pool2_flat, 1024)

        y_conv = slim.fully_connected(h_fc1, 10, activation_fn=None)

    return y_conv


def calc_accuracy(y_, y_conv):
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)
    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    y = model(x_image)
    loss = tf.losses.softmax_cross_entropy(y_, y)
    optimizer = tf.train.AdamOptimizer(1e-4)
    train_step = optimizer.minimize(loss)
    accuracy = calc_accuracy(y_, y)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(1000):
            batch = mnist.train.next_batch(100)
            if i % 100 == 0:
                train_accuracy = sess.run(
                    accuracy, feed_dict={x: batch[0], y_: batch[1]})
                print(train_accuracy)
            sess.run(train_step, feed_dict={x: batch[0], y_: batch[1]})


if __name__ == '__main__':
    main()
