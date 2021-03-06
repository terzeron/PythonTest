#!/usr/bin/env python

import os
import tensorflow.compat.v1 as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#tf.disable_v2_behavior()
tf.compat.v1.disable_eager_execution()

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
W1 = tf.Variable(tf.random_uniform([2, 10], -1.0, 1.0))
W2 = tf.Variable(tf.random_uniform([10, 10], -1.0, 1.0))
W3 = tf.Variable(tf.random_uniform([10, 3], -1.0, 1.0))
# y절편값은 0으로 초기화
b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([10]))
b3 = tf.Variable(tf.zeros([3]))

# 가설 L = X * W1 + b1
L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)
L2 = tf.add(tf.matmul(L1, W2), b2)
L3 = tf.add(tf.matmul(L2, W3), b3)
model = L3
# 비용함수
# cross entropy 함수는 one-hot encoding으로 표현된 classification 문제에 적합함
# mean square error 함수는 실제값과 예측값의 차이를 제곱합해서 최소화하려는 것이 목적
# cross entropy 함수는 유사할수록 0에 logarithmic하게 가까워지고 차이가 클수록 무한대에 가까워짐
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=model))

# 학습
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(100):
    sess.run(train_op, feed_dict={X: x_data, Y: y_data})

    if (step + 1) % 10 == 0:
        print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))


# 학습된 결과 확인
# argmax는 요소 중 가장 큰 값을 골라줌
prediction = tf.argmax(model, axis=1)
target = tf.argmax(Y, axis=1)
print("prediction=", sess.run(prediction, feed_dict={X: x_data}))
print("target=", sess.run(target, feed_dict={Y: y_data}))

# 정확도 측정
is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print("accuracy=%0.2f" % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))
