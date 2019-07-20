import tensorflow as tf


def double(x,):
    return tf.identity(2 * x, name="twice")


def main():
    with tf.name_scope(name="input_x"):
        x = tf.Variable(3, name="x")
    with tf.name_scope(name="func"):
        d = double(x)
        print(d)
    with tf.name_scope(name="again"):
        dd = double(d)
        print(dd)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        res = sess.run(dd)
        print(res)
        res = sess.run(tf.get_default_graph().get_tensor_by_name("again/twice:0"))
        print(res)


if __name__ == '__main__':
    main()
