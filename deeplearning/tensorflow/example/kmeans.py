#https://gist.github.com/uramonk/e9625de0711f29cd0a4b57502648dd86import numpy as np
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""


def main():
    mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)
    full_data_x = mnist.train.images
    num_steps = 50
    batch_size = 1024
    k = 25
    num_classes = 10
    num_features = 784

    X = tf.placeholder(tf.float32, shape=[None, num_features])
    Y = tf.placeholder(tf.float32, shape=[None, num_classes])

    kmeans = KMeans(inputs=X, num_clusters=k,
                    distance_metric='cosine', use_mini_batch=True)
    training_graph = kmeans.training_graph()

    if len(training_graph) > 6:
        (all_scores, cluster_idx, scores, cluster_centers_initialized,
         cluster_centers_var, init_op, train_op) = training_graph
    else:
        (all_scores, cluster_idx, scores, cluster_centers_initialized,
         init_op, train_op) = training_graph

    cluster_idx = cluster_idx[0]
    avg_distance = tf.reduce_mean(scores)

    init_vars = tf.global_variables_initializer()

    sess=tf.Session()
    sess.run(init_vars, feed_dict={X: full_data_x})
    sess.run(init_op, feed_dict={X: full_data_x})

    for i in range(1, num_steps+1):
        _, d, idx = sess.run(
            [train_op, avg_distance, cluster_idx], feed_dict={X: full_data_x})

        if i % 10 == 0 or i == 1:
            print("Step %i, Avg Distance: %f" % (i, d))
    counts = np.zeros(shape=(k, num_classes))
    for i in range(len(idx)):
        counts[idx[i]] += mnist.train.labels[i]

    labels_map = [np.argmax(c) for c in counts]
    labels_map = tf.convert_to_tensor(labels_map)

    cluter_label = tf.nn.embedding_lookup(labels_map, cluster_idx)
    correct_prediction = tf.equal(
        cluter_label, tf.cast(tf.argmax(Y, 1), tf.int32))
    accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    test_x, test_y = mnist.test.images, mnist.test.labels
    print("Test Accucaty", sess.run(accuracy_op, feed_dict={X: test_x, Y: test_y}))

if __name__ == '__main__':
    main()
