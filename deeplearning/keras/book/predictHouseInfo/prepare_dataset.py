"""
predict house price using linear regression with keras
"""
import tensorflow as tf
import keras
from matplotlib import pyplot as plt

# load data
(x_train, y_train), (x_test, y_test) = keras.datasets.boston_housing.load_data()
#x_train.shape == (404, 13)
#y_train.shape == (404,)

# normalize data
x_train_mean = x_train.mean(axis=0)
y_train_mean = y_train.mean()
x_train_std = x_train.std(axis=0)
y_train_std = y_train.std()

x_train = (x_train - x_train_mean) / x_train_std
y_train = (y_train - y_train_mean) / y_train_std

x_test = (x_test - x_train_mean) / x_train_std
y_test = (y_test - y_train_mean) / y_train_std

x = tf.placeholder(tf.float32, (None, 13), name='x')
y = tf.placeholder(tf.float32, (None, 1), name='y')
w = tf.Variable(tf.random_normal((13, 1)))
pred = tf.matmul(x, w)
loss = tf.reduce_mean((y - pred)**2)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_step = optimizer.minimize(loss)
max_epoch = 100
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(max_epoch):
        train_loss, _ = sess.run([loss, train_step], feed_dict={
                                 x: x_train, y: y_train.reshape((-1, 1))})
        print('i: {}, train_loss: {}'.format(i, train_loss))
    test_predict = sess.run(pred, feed_dict={x: x_test})

plt.plot(x_test[:, 5], test_predict, 'bo', label='predict')
plt.plot(x_test[:, 5], y_test, 'ro', label='truth')
plt.legend()
plt.show()
