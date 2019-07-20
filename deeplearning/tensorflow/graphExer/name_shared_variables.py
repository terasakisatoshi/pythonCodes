import tensorflow as tf

counter = 1


def add_bias(x):
    with tf.variable_scope("add_bias", reuse=tf.AUTO_REUSE):
        global counter
        b = tf.get_variable("bias",
                            shape=(),
                            initializer=tf.constant_initializer(counter))
        counter += 1
        return tf.add(x, b, "x_b")


def main():
    x = tf.placeholder(tf.float32, shape=(), name="input")
    with tf.variable_scope("output1"):
        output1 = tf.add_n([add_bias(x) for _ in range(5)])
    with tf.variable_scope("output2"):
        output2 = tf.add_n([add_bias(x) for _ in range(5)])
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        out1, out2 = sess.run([output1, output2], feed_dict={x: 3.0})
        # should be (3.0 + 1.0) * 5
        print(out1, out2)
        tf.summary.FileWriter("logs/shared", tf.get_default_graph())

        print(tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES))
        print(tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES))


if __name__ == '__main__':
    main()
