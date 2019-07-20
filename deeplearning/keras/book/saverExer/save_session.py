import tensorflow as tf


# define variables

a = tf.Variable(1, name='a')
b = tf.assign(a, a + 1)

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a))
    print(sess.run(b))
    saver.save(sess, 'model/model.ckpt')

# load model

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, save_path='model/model.ckpt')
    print(sess.run(a))
    print(sess.run(b))
