from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)

    x = tf.placeholder(tf.float32, [None, 28*28])
    w_1 = tf.Variable(tf.truncated_normal([784, 64], stddev=0.1), name="w1")
    b_1 = tf.Variable(tf.zeros([64], name="b1"))
    h_1 = tf.nn.relu(tf.matmul(x, w_1)+b_1)

    w_2 = tf.Variable(tf.truncated_normal([64, 10], stddev=0.1), name="w2")
    b_2 = tf.Variable(tf.zeros(10), name="b2")

    out = tf.nn.softmax(tf.matmul(h_1, w_2) + b_2)

    y = tf.placeholder(tf.float32, [None, 10])
    loss = tf.reduce_mean(tf.square(y - out))

    train_step = tf.train.GradientDescentOptimizer(
        learning_rate=0.5).minimize(loss)

    correct = tf.equal(tf.argmax(out, axis=1), tf.argmax(y, axis=1))
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        test_images = mnist.test.images
        test_labels = mnist.test.labels

        for i in range(1000):
            step = i + 1
            train_images, train_labels = mnist.train.next_batch(50)
            sess.run(train_step, feed_dict={x: train_images, y: train_labels})

            if step % 10 == 0:
                acc_val = sess.run(accuracy,
                                   feed_dict={x: test_images, y: test_labels})
                print('Step %d: accuracy = %.2f' % (step, acc_val))


if __name__ == '__main__':
    main()
