import tensorflow as tf

m = tf.placeholder(shape=(None, 2), dtype=tf.int32, name='m')

with tf.Session() as sess:
    fm = sess.run(m, feed_dict={m: [[1, 2]]})
    print(fm)
    fm = sess.run(m, feed_dict={m: [[1, 2], [3, 4]]})
    print(fm)
