import tensorflow as tf

a = tf.Variable(1, name='a')
b = tf.constant(1, name='b')
c = tf.assign(a, a + b)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        print('a = ', sess.run(a))
        print('b = ', sess.run(b))
        print('c = ', sess.run(c))
