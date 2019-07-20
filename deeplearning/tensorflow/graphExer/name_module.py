import numpy as np
import tensorflow as tf


def matmul_relu(x):
    with tf.name_scope("matmul_relu"):
        w_shape = (int(x.get_shape()[1]), 1)
        w = tf.Variable(tf.random_normal(w_shape), name="weights")
        b = tf.Variable(0.0, name="bias")
        z = tf.add(tf.matmul(x, w), b, name="z")
        ret = tf.maximum(z, 0., name="relu")
    return ret


def main():
    n_features = 10
    X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
    output = tf.add_n([matmul_relu(X) for _ in range(5)], name="add_relus")
    inp = np.random.random((20, 10))
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        res = sess.run(output, feed_dict={X: inp})
        print(res)
        tf.summary.FileWriter("logs/relu", tf.get_default_graph())


if __name__ == '__main__':
    main()
