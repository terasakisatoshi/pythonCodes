"""
Train MNIST dataset with Multi Layer Perceptron with tf.estimator"""
import numpy as np
import tensorflow as tf

# load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
# format them its type np.float32 or np.int32
X_train = X_train.astype(np.float32).reshape(-1, 28 * 28) / 255.0
X_test = X_test.astype(np.float32).reshape(-1, 28 * 28) / 255.0
y_train = y_train.astype(np.int32)
y_test = y_test.astype(np.int32)
# get validation target from training set
split_threshold = 5000
X_valid, X_train = X_train[:split_threshold], X_train[split_threshold:]
y_valid, y_train = y_train[:split_threshold], y_train[split_threshold:]

feature_cols = [tf.feature_column.numeric_column("X", shape=[28 * 28])]
# define model
dnn_classifier = tf.estimator.DNNClassifier(hidden_units=[300, 100],
                                            n_classes=10,
                                            feature_columns=feature_cols)

# begin training
input_fn = tf.estimator.inputs.numpy_input_fn(x={"X": X_train},
                                              y=y_train,
                                              num_epochs=40,
                                              batch_size=50,
                                              shuffle=True)
dnn_classifier.train(input_fn=input_fn)
# let's evaluate training results
test_input_fn = tf.estimator.inputs.numpy_input_fn(x={"X": X_test},
                                                   y=y_test,
                                                   shuffle=False)
eval_results = dnn_classifier.evaluate(input_fn=test_input_fn)
print(eval_results)

# predict for each data
y_pred_iter = dnn_classifier.predict(input_fn=test_input_fn)
y_pred = list(y_pred_iter)
print(y_pred[0])
