import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import logging
from autils import *

logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)
from lab_utils_common import sigmoid

X, y = load_data()

# print(X[0].reshape(-1,1))
# print(X[0])
def my_dense(a_in, W, b, g):
    # units = W.shape[1]
    # a_out = np.zeros(units)
    # for i in range(units):
    #     w = W[:, i]
    #     z = np.dot(a_in, w) + b[i]
    #     a_out[i] = g(z)
    Z = np.dot(a_in, W) + b   # 线性部分: A_in * W + b
    a_out = g(Z)               # 应用激活函数
    ### END CODE HERE ###
    return (a_out)
# a = np.array([1,2,3]).reshape(-1,1)  #(3,1)
# b = 5
# print(f"(a * b).shape: {(a * b).shape}, \na * b = \n{a * b}")
#
a = np.array([1,2,3]).reshape(-1,1)  #(3,1)
b = 5
print(f"(a + b).shape: {(a + b).shape}, \na + b = \n{a + b}")
# def my_sequential(x,W1,b1,W2,b2,W3,b3):

x_tst = 0.1 * np.arange(1, 3, 1).reshape(2, )  # (1 examples, 2 features)
W_tst = 0.1 * np.arange(1, 7, 1).reshape(2, 3)  # (2 input features, 3 output features)
b_tst = 0.1 * np.arange(1, 4, 1).reshape(3, )  # (3 features)
A_tst = my_dense(x_tst, W_tst, b_tst, sigmoid)
print(A_tst)
a = np.array([1,2,3,4]).reshape(-1,1)
b = np.array([1,2,3,4]).reshape(1,-1)
print(a)
print(b)

print(f"(a + b).shape: {(a * b).shape}, \na + b = \n{a * b}")