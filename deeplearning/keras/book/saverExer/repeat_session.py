import tensorflow as tf

a = tf.Variable(1, name='a')
b = tf.assign(a, a + 1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(b))  # 2
    print(sess.run(b))  # 3

with tf.Session() as sess:
    # enter another session
    # all variables are reset by tf.global_variables_initializer()
    sess.run(tf.global_variables_initializer())
    print(sess.run(b))  # 2
    print(sess.run(b))  # 3
