#!/usr/bin/env python

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)
print(product)

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
