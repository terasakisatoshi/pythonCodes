import logging
import os

import numpy as np
import tensorflow as tf

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_fmt)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# training parameters
n_inputs = 28 * 28
n_hidden1 = 300
n_hidden2 = 100
n_outputs = 10
learning_rate = 0.01
n_epochs = 40
batch_size = 50

# load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# format them its type np.float32 or np.int32
X_train = X_train.astype(np.float32).reshape(-1, 28 * 28) / 255.0
X_test = X_test.astype(np.float32).reshape(-1, 28 * 28) / 255.0
y_train = y_train.astype(np.int32)
y_test = y_test.astype(np.int32)

# get validation target from training set
split_threshold = 5000
X_valid, X_train = X_train[:split_threshold], X_train[split_threshold:]
y_valid, y_train = y_train[:split_threshold], y_train[split_threshold:]


def shuffle_batch(X, y, batch_size):
    rnd_idx = np.random.permutation(len(X))
    n_batches = len(X) // batch_size
    for indices in np.array_split(rnd_idx, n_batches):
        X_batch, y_batch = X[indices], y[indices]
        yield X_batch, y_batch


def neuron_layer(X, n_neurons, name, activation=None):
    with tf.name_scope(name):
        n_inputs = int(X.get_shape()[1])
        stddev = 2 / np.sqrt(n_inputs)
        init = tf.truncated_normal((n_inputs, n_neurons), stddev=stddev)
        W = tf.Variable(init, name="kernel")
        b = tf.Variable(tf.zeros([n_neurons]), name="bias")
        Z = tf.matmul(X, W) + b
        if activation:
            return activation(Z)
        else:
            return Z


def mlp_model(X, name="dnn"):
    with tf.name_scope("dnn"):
        hidden1 = neuron_layer(X, n_hidden1, name="hidden1", activation=tf.nn.relu)
        hidden2 = neuron_layer(hidden1, n_hidden2, name="hidden2", activation=tf.nn.relu)
        logits = neuron_layer(hidden2, n_outputs, name="outputs")
    return logits


def train():

    X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
    y = tf.placeholder(tf.int32, shape=(None), name="y")

    logits = mlp_model(X, name="dnn")

    with tf.name_scope("loss"):
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)
        loss = tf.reduce_mean(cross_entropy, name="loss")
    with tf.name_scope("train"):
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        training_op = optimizer.minimize(loss)
    with tf.name_scope("eval"):
        correct = tf.nn.in_top_k(logits, y, 1)
        accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(n_epochs):
            for batch, (X_batch, y_batch) in enumerate(shuffle_batch(X_train, y_train, batch_size)):
                _, acc_batch = sess.run([training_op, accuracy], feed_dict={X: X_batch, y: y_batch})
                acc_val = accuracy.eval(feed_dict={X: X_valid, y: y_valid})
                logger.info("batch {}, Val accuracy: {}".format(batch, acc_val))
            logger.info("epoch {}, Batch accuracy {}, Val accuracy {}".format(epoch, acc_batch, acc_val))
        save_dir = "model_dir"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        save_path = saver.save(sess, os.path.join(save_dir, "model.ckpt"))


def predict():
    X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
    logits = mlp_model(X, name="dnn")

    saver = tf.train.Saver()
    X_new_scaled = X_test[:20]
    with tf.Session() as sess:
        saver.restore(sess, "model_dir")
        Z = sess.run(logits, feed_dict={X: X_new_scaled})
        y_pred = np.argmax(Z, axis=1)
    print("Predicted classes", y_pred)
    print("Actual classes", y_test[:20])
    print([y_p == y_gt for y_p, y_gt in zip(y_pred, y_test)])


def main():
    train()
    predict()
if __name__ == '__main__':
    main()
