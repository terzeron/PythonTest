#!/usr/bin/env python

import tensorflow as tf

state = tf.Variable(10, name="counter")

two = tf.constant(2)
new_value = tf.add(state, two)
update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
