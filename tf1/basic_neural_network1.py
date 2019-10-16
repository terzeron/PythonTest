#!/usr/bin/env python

import os
import tensorflow.compat.v1 as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#tf.disable_v2_behavior()

# 두 가지 속성을 가지는 6개의 데이터
x_data = np.array([
    [0, 0], [1, 0], [1, 1], [0, 0], [0, 0], [0, 1]
    ])
# 6개의 데이터가 3가지 카테고리로 분류됨 (one-hot encoding)
y_data = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
    ])

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# -1.0부터 1.0 사이의 정규분포에 따르는 값들로 초기화된 2x3 배열
W = tf.Variable(tf.random_uniform([2, 3], -1.0, 1.0))
# y절편값은 0으로 초기화
b = tf.Variable(tf.zeros([3]))

# 가설 L = X * W + b
L = tf.add(tf.matmul(X, W), b)
# activation function
L = tf.nn.relu(L)
# 가설을 softmax를 이용하여 총 합이 1.0이 되도록(확률값으로) 변환
model = tf.nn.softmax(L)
# 비용함수
# cross entropy 함수는 one-hot encoding으로 표현된 classification 문제에 적합함
# mean square error 함수는 실제값과 예측값의 차이를 제곱합해서 최소화하려는 것이 목적
# cross entropy 함수는 실제값과 log(예측값)*(-1)을 곱해서 최소화하려는 것이 목적
# 가정: 실제값은 0이거나 1임
# 실제값이 1일 때, 
#   예측값이 0에 가까워질수록 비용함수값은 1에 가까워지고
#   예측값이 1에 가까워질수록 비용함수값은 0에 가까워짐
# 실제값이 0일 때,
#   예측값과 상관없이 0이 됨
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train_op = optimizer.minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for step in range(10000):
        sess.run(train_op, feed_dict={X: x_data, Y: y_data})

        if (step + 1) % 1000 == 0:
            print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))

    prediction = tf.argmax(model, axis=1)
    target = tf.argmax(Y, axis=1)
    print("prediction=", sess.run(prediction, feed_dict={X: x_data}))
    print("target=", sess.run(target, feed_dict={Y: y_data}))

    is_correct = tf.equal(prediction, target)
    accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
    print("accuracy=%0.2f" % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))
