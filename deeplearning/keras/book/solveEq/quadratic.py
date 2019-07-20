import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt


x = tf.Variable(0., name='x')
func = lambda x: (x - 1)**2

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_step = optimizer.minimize(func(x))

xs = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(20):
        sess.run(train_step)
        print('x = ', sess.run(x))
        xs.append(sess.run(x))
    print('x = ', sess.run(x))

# visualize result
plt.plot(np.linspace(0, 2, 50), func(np.linspace(0, 2, 50)))
xs = np.asarray(xs)
ys = func(xs)
plt.plot(xs, ys, 'o')
plt.show()
