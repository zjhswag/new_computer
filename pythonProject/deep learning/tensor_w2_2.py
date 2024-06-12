import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model

np.set_printoptions(precision=2)
from lab_utils_multiclass_TF import *
# 对比softmax 和 linear 处理上的的不同，一般用linear。
import logging

logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

classes = 4
m = 100
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
std = 1.0
X_train, y_train = make_blobs(n_samples=m, centers=centers, cluster_std=std, random_state=30)  # 得到数据洁群
print(X_train.shape)
# print(y_train) #de dao 0,1,2,3的序列
# plt_mc(X_train,y_train,classes, centers, std=std)


tf.random.set_seed(1234)  # applied to achieve consistent results
model = Sequential(
    [
        Dense(2, activation='relu', name="L1"),
        Dense(4, activation='softmax', name="L2")
    ]
)
# 注意这里输出是线性激活函数，代表着输出a,如果是softmax就会存在精度误差，输出z,在带入误差函数计算就会导致误差较大
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=tf.keras.optimizers.Adam(0.01),
    metrics=['accuracy']
)

model.fit(
    X_train, y_train,
    epochs=200
)

layer_outputs = model.get_layer('L1').output
intermediate_model = Model(inputs=model.input, outputs=layer_outputs)

# 使用新模型对输入数据X_train进行预测
L1_output = intermediate_model.predict(X_train)

# 打印"L1"层的输出
# print(L1_output.shape)


# l2 = model.get_layer('L2')
# w2,b2 = l2.get_weights()
# print(w2,b2,w2.shape)

# np.arange()
y = model.predict(X_train)
y1 = np.argmax(y, axis=1)
fig, ax = plt.subplots(1, 2, figsize=(4, 4))

for i in range(classes):
    idx = np.where(y1 == i)
    date = np.where(y_train == i)
    label1 = "p{}".format(i)
    label = "c{}".format(i)
    ax[0].scatter(X_train[idx, 0], X_train[idx, 1], marker='o', label=label)

    ax[1].scatter(X_train[date, 0], X_train[date, 1], marker='s', label=label1)
    ax[0].legend()
    ax[1].legend()

# plt.show()


# plt_cat_mc(X_train, y_train, model, classes)

l1 = model.get_layer("L1")
W1, b1 = l1.get_weights()

# print(W1.shape) # （2，2）
# print(W1)

# plt_layer_relu(X_train, y_train.reshape(-1,), W1, b1, classes)

l2 = model.get_layer("L2")
W2, b2 = l2.get_weights()

# # create the 'new features', the training examples after L1 transformation

Xl2 = np.zeros_like(X_train)
Xl2 = np.maximum(0, np.dot(X_train, W1) + b1)

plt_output_layer_linear(Xl2, y_train.reshape(-1, ), W2, b2, classes,
                        x0_rng=(-0.25, np.amax(Xl2[:, 0])), x1_rng=(-0.25, np.amax(Xl2[:, 1])))
