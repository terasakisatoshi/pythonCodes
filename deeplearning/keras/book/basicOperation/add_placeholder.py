import tensorflow as tf

a = tf.placeholder(dtype=tf.int32, name='a')
b = tf.constant(1, name='b')
c = a + b

with tf.Session() as sess:
    print(sess.run(c, feed_dict={a: 1}))
