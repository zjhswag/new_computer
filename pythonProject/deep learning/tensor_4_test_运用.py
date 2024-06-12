import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from autils import *

import logging

logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

X, y = load_data()
# print ('The first element of X is: ', X[0],X[0].shape)
# print ('The first element of y is: ', y[0,0])
print('The shape of X is: ' + str(X.shape))
# print ('The shape of y is: ' + str(y.shape))

# import warnings
#
# warnings.simplefilter(action='ignore', category=FutureWarning)
# # You do not need to modify anything in this cell
#
# m, n = X.shape

# fig, axes = plt.subplots(8, 8, figsize=(8, 8))
# fig.tight_layout(pad=0.1)
# # print(axes.flat)
# for i, ax in enumerate(axes.flat):
#     # for  ax  in axes.flat: # 这个也可以，有了i就能知道遍历到第几个图了
#
#     # Select random indices
#     # print(i)
#     random_index = np.random.randint(m)
#     # print(ax.get_position())
#     # Select rows corresponding to the random indices and
#     # reshape the image
#     X_random_reshaped = X[random_index].reshape((20, 20)).T
#
#     # Display the image
#     ax.imshow(X_random_reshaped, cmap='gray')
#     # Display the label above the image
#     ax.set_title(y[random_index, 0])
#     ax.set_axis_off()

# plt.show()

# GRADED CELL: Sequential model
# w有多少列，就输出给下一层多少个。行取决于上一层输入
model = Sequential(
    [
        tf.keras.Input(shape=(400,)),  # specify input size
        Dense(units=25, activation='sigmoid', name='l1'),
        Dense(units=15, activation='sigmoid', name='l2'),
        Dense(units=1, activation='sigmoid', name='l3')

    ], name="my_model"
)
# model.summary()
[layer1, layer2, layer3] = model.layers
W1, b1 = layer1.get_weights()
W2, b2 = layer2.get_weights()
W3, b3 = layer3.get_weights()
print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")  # 400，25
print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")  # 25，15
print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")  # 1 5，1

# print(model.layers[0].weights)

model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy']
)

model.fit(
    X, y,
    epochs=20
)
predictions = model.predict(X)  # 获取模型的预测结果
predictions = (predictions >= 0.5).astype(int)  # 将预测结果转换为 0 或 1

# 计算准确率
accuracy = np.mean(predictions == y)
print(f"模型准确率: {accuracy * 100:.2f}%")
pre = np.zeros(1000)
loss, accuracy = model.evaluate(X, y)
print(f"测试集准确率: {accuracy * 100:.2f}%,loss为{loss}")
# print(pre.shape)

# pre = model.predict(X)
# pre = (pre >= 0.5).astype(int)
# sum = 0
# for i in range(1000):
#     sum += np.abs(pre[i]-y[i,0])
#
# print(sum)
# print(sum1)

# W1,b1 = layer1.get_weights()
# W2,b2 = layer2.get_weights()
# W3,b3 = layer3.get_weights()
# print(W3,b3)
# print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
# print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
# print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
# You do not need to modify anything in this cell

m, n = X.shape

fig, axes = plt.subplots(8, 8, figsize=(8, 8))
fig.tight_layout(pad=0.1, rect=[0, 0.03, 1, 0.92])  # [left, bottom, right, top]

for i, ax in enumerate(axes.flat):
    # Select random indices
    random_index = np.random.randint(m)

    # Select rows corresponding to the random indices and
    # reshape the image
    X_random_reshaped = X[random_index].reshape((20, 20)).T

    # Display the image
    ax.imshow(X_random_reshaped, cmap='gray')

    # Predict using the Neural Network
    prediction = model.predict(X[random_index].reshape(1, 400))
    if prediction >= 0.5:
        yhat = 1
    else:
        yhat = 0

    # Display the label above the image
    ax.set_title(f"{y[random_index, 0]},{yhat}")
    ax.set_axis_off()
fig.suptitle("Label, yhat", fontsize=16)
plt.show()
