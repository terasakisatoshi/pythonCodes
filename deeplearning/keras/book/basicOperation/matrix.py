import tensorflow as tf

a = tf.constant([[1, 2],
                 [3, 4]], name='a')

b = tf.constant([[1],
                 [2]], name='b')

c = tf.matmul(a, b)

print('shape of a = ', a.shape)
print('shape of b = ', b.shape)
print('shape of c = ', c.shape)

with tf.Session() as sess:
    print('a=\n', sess.run(a))
    print('b=\n', sess.run(b))
    print('c=\n', sess.run(c))
