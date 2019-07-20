"""
Simple hello world using TensorFlow 
The op is added as a node to the default graph.
The value returned by the constructor represents the output of the Constant op.
"""

import tensorflow as tf 

def main():
    hello=tf.constant('Hello, TensorFlow')
    #start th session
    session=tf.Session()
    #run the op
    session.run(hello)
    
if __name__ == '__main__':
    main()
