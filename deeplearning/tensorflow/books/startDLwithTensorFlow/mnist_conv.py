from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

SAME = "SAME"


def main():
    mnist = input_data.read_data_sets("data/", one_hot=True)
    x = tf.placeholder(tf.float32, [None, 28 * 28])
    y = tf.placeholder(tf.float32, [None, 10])
    img = tf.reshape(x, [-1, 28, 28, 1])

    with tf.name_scope("convolution2d-1"):
        filter1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
        conv1 = tf.nn.conv2d(img, filter1, strides=[1, 1, 1, 1], padding=SAME)
        b1 = tf.Variable(tf.constant(0.1, shape=[32]))
        h_conv1 = tf.nn.relu(conv1 + b1)
        h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[
                                 1, 2, 2, 1], padding=SAME)

    with tf.name_scope("convolution2d-2"):
        filter2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
        conv2 = tf.nn.conv2d(h_pool1, filter2, strides=[
                             1, 1, 1, 1], padding=SAME)
        b2 = tf.Variable(tf.constant(0.1, shape=[64]))
        h_conv2 = tf.nn.relu(conv2 + b2)
        h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[
                                 1, 2, 2, 1], padding=SAME)

    with tf.name_scope("fully-connected"):
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
        w_fc1 = tf.Variable(tf.truncated_normal(
            [7 * 7 * 64, 1024], stddev=0.1))

        b_cf1 = tf.Variable(tf.constant(0.1, shape=[1024]))
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_cf1)

    with tf.name_scope("output"):
        w_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
        b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))
        out = tf.nn.softmax(tf.matmul(h_fc1, w_fc2) + b_fc2)

    loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(out + 1e-5), axis=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
    correct = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        test_images = mnist.test.images
        test_labels = mnist.test.labels

        for step in range(1000):
            train_images, train_labels = mnist.train.next_batch(50)
            sess.run(train_step, feed_dict={x: train_images, y: train_labels})
            if step % 100 == 0:
                acc_val = sess.run(accuracy, feed_dict={
                                   x: test_images, y: test_labels})
                print(acc_val)


if __name__ == '__main__':
    main()
