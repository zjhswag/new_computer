import numpy as np
import matplotlib.pyplot as plt
from keras import activations
from matplotlib.gridspec import GridSpec
plt.style.use('./deeplearning.mplstyle')
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU
from tensorflow.keras.activations import linear, relu, sigmoid

from matplotlib.widgets import Slider
from lab_utils_common import dlc
# from autils import plt_act_trio
from lab_utils_relu import *
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


# _ = plt_relu_ex()

def plt_act_trio():
    X = np.linspace(-5,5,100)
    fig,ax = plt.subplots(1,3, figsize=(10,4))
    widgvis(fig)
    ax[0].plot(X,tf.keras.activations.linear(X))
    ax[0].axvline(0, lw=0.3, c="black")    # 设置竖直线，第一个参数为0,说明线为y的位置
    ax[0].axhline(0, lw=0.3, c="black")
    ax[0].set_title("linear")
    ax[1].plot(X,tf.keras.activations.sigmoid(X))
    ax[1].axvline(0, lw=0.3, c="black")
    ax[1].axhline(0, lw=0.3, c="black")
    ax[1].set_title("sigmoid")
    ax[2].plot(X,tf.keras.activations.relu(X))
    ax[2].axhline(0, lw=0.3, c="black")
    ax[2].axvline(0, lw=0.3, c="black")
    ax[2].set_title("relu")
    fig.suptitle("Common Activation Functions", fontsize=14)
    fig.tight_layout(pad=1)
    plt.show()


# plt_act_trio()
# print(np.pi)
X = np.linspace(0,2*np.pi, 100)
y = np.cos(X)+1
y[50:100]=0
# # # y[50] = 1
# # fig,ax = plt.subplots(1,1, figsize=(2,2))
# # widgvis(fig)
# # ax.plot(X,y)
# # plt.show()
#
w10 = np.array([[-1]])
b10 = np.array([2.6])
d10 = Dense(1, activation = "linear", input_shape = (1,), weights=[w10,b10])
z10 = d10(X.reshape(-1,1))
a10 = relu(z10)
#
#
def plt_act1(y, z, a):
    fig, ax = plt.subplots(1, 3, figsize=(8, 4))
    widgvis(fig)
    ax[0].plot(X, y, label="target")
    ax[0].axvline(0, lw=0.3, c="black")
    ax[0].axhline(0, lw=0.3, c="black")
    ax[0].set_title("y - target")
    ax[1].plot(X, y, label="target")
    ax[1].plot(X, z, c=dlc["dldarkred"], label="z")
    ax[1].axvline(0, lw=0.3, c="black")
    ax[1].axhline(0, lw=0.3, c="black")
    ax[1].set_title("z = wX+b")
    ax[1].legend(loc="upper center")
    ax[2].plot(X, y, label="target")
    ax[2].plot(X, a, c=dlc["dldarkred"], label="ReLu(z)")
    ax[2].axhline(0, lw=0.3, c="black")
    ax[2].axvline(0, lw=0.3, c="black")
    ax[2].set_title("with relu")
    ax[2].legend()
    fig.suptitle("Role of Activation", fontsize=14)
    fig.tight_layout(pad=1)
    return (ax)


def plt_add_notation(ax):
    ax[1].annotate(s="matches\n here", xy=(1.5, 1.0),xytext=(0.1, -1.5), fontsize=10,arrowprops=dict(facecolor=dlc["dlpurple"], width=2, headwidth=8))
    ax[1].annotate(s="but not\n here", xy=(5, -2.5),xytext=(1, -3), fontsize=10,arrowprops=dict(facecolor=dlc["dlpurple"], width=2, headwidth=8))
    ax[2].annotate(s="ReLu\n 'off'", xy=(2.6, 0),xytext=(0.1, 0.1), fontsize=10,
                   arrowprops=dict(facecolor=dlc["dlpurple"], width=2, headwidth=8))


ax = plt_act1(y, z10, a10)
plt_add_notation(ax)
plt.show()


