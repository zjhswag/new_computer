# 避免softmax处理指数时，溢出，改成减去max的值
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('./deeplearning.mplstyle')
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from sklearn.datasets import make_blobs

from matplotlib.widgets import Slider
from lab_utils_common import dlc
from lab_utils_softmax import plt_softmax
import logging

logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

# 溢出
def my_softmax(z):
    ez = np.exp(z)
    sm = ez / np.sum(ez)
    return sm

# 修改后不溢出
def my_softmax_ns(z):
    """numerically stablility improved"""
    bigz = np.max(z)
    ez = np.exp(z-bigz)              # minimize exponent
    sm = ez/np.sum(ez)
    return sm


for z in [500, 600, 700, 800]:
    ez = np.exp(z)
    zs = "{" + f"{z}" + " }"
    print(f"e^{zs} = {ez:0.2e}")

z_tmp = np.array([[500,600,700,800]])
print(my_softmax(z_tmp))
print(z_tmp.shape)
z_tmp = np.array([500,600,700,800], dtype=np.float64)  # 注意这个地方精度设置为64，才能输出想得到的数据。
print(tf.nn.softmax(z_tmp).numpy(), "\n", my_softmax_ns(z_tmp))



#
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
X_train, y_train = make_blobs(n_samples=2000, centers=centers, cluster_std=1.0,random_state=30)

model = Sequential(
    [
        Dense(25, activation = 'relu'),
        Dense(15, activation = 'relu'),
        Dense(4, activation = 'softmax')    # < softmax activation here
    ]
)
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy']
)

model.fit(
    X_train,y_train,
    epochs=100
)

p_nonpreferred = model.predict(X_train)
y1 = np.argmax(p_nonpreferred,axis=1)
# print(y1[:])
