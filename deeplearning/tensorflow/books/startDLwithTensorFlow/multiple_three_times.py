import tensorflow as tf 

a = tf.constant(3, name="const1")
b = tf.Variable(0, name="var")

add = tf.add(a,b)
assign = tf.assign(b, add)
c = tf.placeholder(tf.int32, name = "input")
mul=tf.multiply(assign,c)
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        print(sess.run(mul, feed_dict={c:3}))