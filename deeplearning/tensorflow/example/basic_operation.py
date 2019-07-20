"""
Basic Operation example using TensorFlow Library
"""

import tensorflow as tf


def constant_operation():
    pass
    # Basic constant operations
    # The value returned by the constructor represents the output of the constant op.
    a = tf.constant(2)
    b = tf.constant(3)

    with tf.Session() as sess:
        res=sess.run(a+b)
        print(res)
        res=sess.run(a*b)
        print(res)

def variable_operation():
    """
    Basic Operations with variable as graph input 
    The value returned by the constructor represents the output of the Variable op.
    """
    a = tf.placeholder(tf.int16)
    b = tf.placeholder(tf.int16)
    # Define some operators
    add = tf.add(a, b)
    mul = tf.multiply(a, b)
    # Launch the default graph
    with tf.Session() as sess:
        res=sess.run(add, feed_dict={a: 2, b: 3})
        print(res)
        res=sess.run(mul, feed_dict={a: 2, b: 3})
        print(res)

def matrix_operation():
    matrix1 = tf.constant([[3, 3]])
    matrix2 = tf.constant([[2], [2]])
    mat_mul = tf.matmul(matrix1, matrix2)
    with tf.Session() as sess:
        result = sess.run(mat_mul)
        print(result)


def main():
    constant_operation()
    variable_operation()
    matrix_operation()


if __name__ == '__main__':
    main()
