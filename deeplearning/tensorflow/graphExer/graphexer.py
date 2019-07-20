import os
import tensorflow as tf
from tensorflow.python.framework import graph_util


def save_val():
    with tf.name_scope(name="simple"):
        x = tf.Variable(3, name="x")
        y = tf.Variable(4, name="y")
        f = tf.identity(x * x + y * y, name="f")

    saver = tf.train.Saver()
    if not os.path.exists("ckpt"):
        os.mkdir("ckpt")
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(f.eval())
        saver.save(sess, "ckpt/val_save")


def restore_val():
    with tf.name_scope(name="simple"):
        xx = tf.Variable(3, name="x")
        yy = tf.Variable(4, name="y")
        ff = tf.identity(xx * xx + yy * yy, name="f")

    saver = tf.train.Saver()
    ckpt_path = tf.train.latest_checkpoint("ckpt")
    print("ckpt_path=", ckpt_path)
    with tf.Session() as sess:
        saver.restore(sess, ckpt_path)
        g = sess.graph
        gdef = g.as_graph_def()
        tf.train.write_graph(gdef, 'ckpt', "graph.pb", as_text=False)


def main():
    save_val()
    tf.reset_default_graph()
    restore_val()


if __name__ == '__main__':
    main()
