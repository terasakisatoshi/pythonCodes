from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)

    x = tf.placeholder(tf.float32, [None, 28*28])
    img = tf.reshape(x, [-1,28,28,1])
    tf.summary.image("input_data", img, 10)

    with tf.name_scope("hidden"):
        w_1 = tf.Variable(tf.truncated_normal(
            [784, 64], stddev=0.1), name="w1")
        b_1 = tf.Variable(tf.zeros([64], name="b1"))
        h_1 = tf.nn.relu(tf.matmul(x, w_1)+b_1)
        tf.summary.histogram("w_1", w_1)

    with tf.name_scope("output"):
        w_2 = tf.Variable(tf.truncated_normal([64, 10], stddev=0.1), name="w2")
        b_2 = tf.Variable(tf.zeros(10), name="b2")
        out = tf.nn.softmax(tf.matmul(h_1, w_2) + b_2)

    y = tf.placeholder(tf.float32, [None, 10])

    with tf.name_scope("loss"):
        loss = tf.reduce_mean(tf.square(y - out))
        tf.summary.scalar("loss", loss)

    with tf.name_scope("train"):
        train_step = tf.train.GradientDescentOptimizer(
            learning_rate=0.5).minimize(loss)

    with tf.name_scope("accuracy"):
        correct = tf.equal(tf.argmax(out, axis=1), tf.argmax(y, axis=1))
        accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
        tf.summary.scalar("accuracy", accuracy)

    init = tf.global_variables_initializer()
    summary_op = tf.summary.merge_all()

    with tf.Session() as sess:
        summary_writer=tf.summary.FileWriter("logs", sess.graph)
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
                summary_str = sess.run(summary_op, feed_dict={x:test_images, y:test_labels})
                summary_writer.add_summary(summary_str, step)

if __name__ == '__main__':
    main()
