"""
# ==============================================================================
# MINIMAL TRANSFER LEARNING EXAMPLE USING PRETRAINED INCEPTION V3 MODEL
# Author: Ronny Restrepo
# Origin: http://ronny.rest/blog/post_2017_10_13_tf_transfer_learning
# License: MIT License
# Copyright (c) 2017 Ronny Restrepo
# ==============================================================================
"""
from __future__ import print_function, division
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim.nets

SNAPSHOT_FILE = "snapshot.ckpt"
PRETRAINED_SNAPSHOT_FILE = "inception_v3.ckpt"

# somewhere to store the tensorboard files - to visualise the graph
TENSORBOARD_DIR = "tensorboard_dir"

# IMAGE SETTINGS
IMG_WIDTH, IMG_HEIGHT = [299, 299]  # Dimensions required by inception V3
N_CHANNELS = 3                    # Number of channels required by inception V3
N_CLASSES = 10                    # Change N_CLASSES to suit your needs

graph = tf.Graph()
with graph.as_default():
    # INPUTS
    with tf.name_scope("inputs") as scope:
        input_dims = (None, IMG_HEIGHT, IMG_WIDTH, N_CHANNELS)
        tf_X = tf.placeholder(tf.float32, shape=input_dims, name="X")
        tf_Y = tf.placeholder(tf.int32, shape=[None], name="Y")
        tf_alpha = tf.placeholder_with_default(0.001, shape=None, name="alpha")
        tf_is_training = tf.placeholder_with_default(
            False, shape=None, name="is_training")

    # PREPROCESSING STEPS
    with tf.name_scope("preprocess") as scope:
        scaled_inputs = tf.div(tf_X, 255., name="rescaled_inputs")

    # BODY
    arg_scope = tf.contrib.slim.nets.inception.inception_v3_arg_scope()
    with tf.contrib.framework.arg_scope(arg_scope):
        tf_logits, end_points = tf.contrib.slim.nets.inception.inception_v3(
            scaled_inputs,
            num_classes=N_CLASSES,
            is_training=tf_is_training,
            dropout_keep_prob=0.8)

    # PREDICTIONS
    tf_preds = tf.to_int32(tf.argmax(tf_logits, axis=-1), name="preds")

    # LOSS - Sums all losses (even Regularization losses)
    with tf.variable_scope('loss') as scope:
        unrolled_labels = tf.reshape(tf_Y, (-1,))
        tf.losses.sparse_softmax_cross_entropy(labels=unrolled_labels,
                                               logits=tf_logits)
        tf_loss = tf.losses.get_total_loss()

    # OPTIMIZATION - Also updates batchnorm operations automatically
    with tf.variable_scope('opt') as scope:
        tf_optimizer = tf.train.AdamOptimizer(tf_alpha, name="optimizer")
        update_ops = tf.get_collection(
            tf.GraphKeys.UPDATE_OPS)  # for batchnorm
        with tf.control_dependencies(update_ops):
            tf_train_op = tf_optimizer.minimize(tf_loss, name="train_op")

    # PRETRAINED SAVER SETTINGS
    # Lists of scopes of weights to include/exclude from pretrained snapshot
    pretrained_include = ["InceptionV3"]
    pretrained_exclude = ["InceptionV3/AuxLogits", "InceptionV3/Logits"]

    # PRETRAINED SAVER - For loading pretrained weights on the first run
    pretrained_vars = tf.contrib.framework.get_variables_to_restore(
        include=pretrained_include,
        exclude=pretrained_exclude)
    tf_pretrained_saver = tf.train.Saver(
        pretrained_vars, name="pretrained_saver")

    # MAIN SAVER - For saving/restoring your complete model
    tf_saver = tf.train.Saver(name="saver")

    # TENSORBOARD - To visialize the architecture
    with tf.variable_scope('tensorboard') as scope:
        tf_summary_writer = tf.summary.FileWriter(TENSORBOARD_DIR, graph=graph)
        tf_dummy_summary = tf.summary.scalar(name="dummy", tensor=1)


def initialize_vars(session):
    # INITIALIZE VARS
    if tf.train.checkpoint_exists(SNAPSHOT_FILE):
        print(" Loading from Main Checkpoint")
        tf_saver.restore(session, SNAPSHOT_FILE)
    else:
        print("Initializing from Pretrained Weights")
        session.run(tf.global_variables_initializer())
        tf_pretrained_saver.restore(session, PRETRAINED_SNAPSHOT_FILE)


with tf.Session(graph=graph) as sess:
    n_epochs = 2
    print_every = 32
    batch_size = 2  # small batch size so inception v3 can be run on laptops
    steps_per_epoch = len(X_train) // batch_size

    initialize_vars(session=sess)

    for epoch in range(n_epochs):
        print("----------------------------------------------")
        print("EPOCH {}/{}".format(epoch + 1, n_epochs))
        print("----------------------------------------------")
        for step in range(steps_per_epoch):
            # EXTRACT A BATCH OF TRAINING DATA
            X_batch = X_train[batch_size * step: batch_size * (step + 1)]
            Y_batch = Y_train[batch_size * step: batch_size * (step + 1)]

            # RUN ONE TRAINING STEP - feeding batch of data
            feed_dict = {tf_X: X_batch,
                         tf_Y: Y_batch,
                         tf_alpha: 0.0001,
                         tf_is_training: True}
            loss, _ = sess.run([tf_loss, tf_train_op], feed_dict=feed_dict)

            # PRINT FEED BACK - once every `print_every` steps
            if (step + 1) % print_every == 0:
                print("STEP: {: 4d}  LOSS: {:0.4f}".format(step, loss))

        # SAVE SNAPSHOT - after each epoch
        tf_saver.save(sess, SNAPSHOT_FILE)
