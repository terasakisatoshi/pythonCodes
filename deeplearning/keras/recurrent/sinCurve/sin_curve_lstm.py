import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


def inference(x, n_batch, maxlen=None, n_hidden=None, n_out=None):
    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev=0.01)
        return tf.Variable(initial)

    def bias_variable(shape):
        initial = tf.zeros(shape, dtype=tf.float32)
        return tf.Variable(initial)

    cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
    initial_state = cell.zero_state(n_batch, tf.float32)

    state = initial_state
    outputs = []
    with tf.variable_scope('LSTM', reuse=tf.AUTO_REUSE):
        for t in range(maxlen):
            (cell_output, state) = cell(x[:, t, :], state)
            outputs.append(cell_output)

    output = outputs[-1]

    V = weight_variable([n_hidden, n_out])
    c = bias_variable([n_out])
    y = tf.matmul(output, V) + c
    return y


class EarlyStopping():

    def __init__(self, max_count=0, verbose=0):
        self.counter = 0
        self.prev_loss = float('inf')
        self.max_count = max_count
        self.verbose = verbose

    def validate(self, current_loss):
        if self.prev_loss < current_loss:
            self.counter += 1
            if self.counter > self.max_count:
                if self.verbose:
                    print("Early Stopping")
                return True
        else:
            self.counter = 0
            self.prev_loss = current_loss
        return False


def sin(x, T=100):
    return np.sin(2.0 * np.pi * x / T)


def toy_problem(T=100, ampl=0.05):
    x = np.arange(0, 2 * T + 1)
    noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))
    return sin(x) + noise


def generate_data(T, maxlen):
    length = 2 * T
    f = toy_problem(T)
    maxlen = 25
    data = []
    target = []

    for i in range(0, length - maxlen + 1):
        data.append(f[i:maxlen + i])
        target.append(f[i + maxlen])

    X = np.array(data).reshape(len(data), maxlen, 1)
    Y = np.array(target).reshape(len(data), 1)
    return X, Y


def lossfn(y, t):
    mse = tf.reduce_mean(tf.square(y - t))
    return mse


def training(loss):
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001, beta1=0.9, beta2=0.999)
    train_step = optimizer.minimize(loss)
    return train_step


def train():
    # prepare dataset
    maxlen = 25
    T = 100
    length = 2 * T
    X, Y = generate_data(T, maxlen)
    N_train = int(X.shape[0] * 0.9)
    N_validation = X.shape[0] - N_train
    print(N_train, N_validation)
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation)

    # define model
    n_in = len(X[0][0])
    n_hidden = 30
    n_out = len(Y[0])

    x = tf.placeholder(tf.float32, shape=[None, maxlen, n_in])
    t = tf.placeholder(tf.float32, shape=[None, n_out])
    n_batch = tf.placeholder(tf.int32, shape=[])

    y = inference(x, n_batch, maxlen=maxlen, n_hidden=n_hidden, n_out=n_out)
    loss = lossfn(y, t)
    train_step = training(loss)
    early_stopping = EarlyStopping(max_count=10, verbose=True)
    history = {"val_loss": []}

    # training sequence
    epochs = 500
    batch_size = 10

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        n_batches = N_train // batch_size
        for e in range(epochs):
            X_shuffled, Y_shuffled = shuffle(X_train, Y_train)
            for i in range(n_batches):
                start = i * batch_size
                end = start + batch_size

                sess.run(train_step, feed_dict={
                    x: X_shuffled[start:end],
                    t: Y_shuffled[start:end],
                    n_batch: batch_size
                })
            val_loss = loss.eval(session=sess, feed_dict={
                x: X_validation,
                t: Y_validation,
                n_batch: N_validation
            })

            history["val_loss"].append(val_loss)
            print("epoch", e, "validation loss", val_loss)

            if early_stopping.validate(val_loss):
                break

        truncate = maxlen
        Z = X[:1]
        f = toy_problem(T)
        original = [f[i] for i in range(maxlen)]
        predicted = [None] * maxlen

        for i in range(length - maxlen + 1):
            z_ = Z[-1:]
            y_ = y.eval(session=sess, feed_dict={x: Z[-1:], n_batch: 1})
            sequence_ = np.concatenate((z_.reshape(maxlen, n_in)[1:], y_), axis=0)
            sequence_ = sequence_.reshape(1, maxlen, n_in)
            Z = np.append(Z, sequence_, axis=0)
            predicted.append(y_.reshape(-1))

    # Visualize data
    plt.figure()
    plt.ylim([-1.5, 1.5])
    plt.plot(toy_problem(T, ampl=0), linestyle="dotted", color="#aaaaaa")
    plt.plot(original, linestyle="dashed", color="black")
    plt.plot(predicted, color="black")
    plt.show()


def main():
    np.random.seed(0)
    tf.set_random_seed(1234)
    train()


if __name__ == '__main__':
    main()
