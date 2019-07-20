import tensorflow as tf

log_dir = "log"

a = tf.constant(1, name='a')
b = tf.constant(1, name='b')

c = a + b

graph = tf.get_default_graph()
with tf.summary.FileWriter(log_dir) as writer:
    writer.add_graph(graph)
