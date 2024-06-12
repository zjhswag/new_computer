import random

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.activations import linear, relu, sigmoid

import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')

import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

from public_tests import *

from autils2 import *
from lab_utils_softmax import plt_softmax
np.set_printoptions(precision=2)


def my_softmax(z):
    c = max(z)
    z = np.exp(z-c)
    z = z/np.sum(z)
    return z


X, y = load_data()

# print ('The first element of X is: ', X[0].shape)
# print ('The shape of X is: ' + str(X.shape)) (5000,400)
# print ('The shape of y is: ' + str(y.shape))  (5000,1)


# m,n=X.shape
# fig,axes = plt.subplots(8,8,figsize=(5,5))
# fig.tight_layout(pad=0.13,rect=[0, 0.03, 1, 0.91]) #[left, bottom, right, top]

# np.random.seed(1)

# for i,ax in enumerate(axes.flat):
#     random_index = np.random.randint(m)
#     x_reshape = X[random_index].reshape(20,20).T
#     ax.imshow(x_reshape,cmap='gray')
#     ax.set_title(y[random_index,0])
#     ax.set_axis_off()
#     fig.suptitle("Label, image", fontsize=14)
#
# plt.show()

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

tf.random.set_seed(1234)

model = Sequential(
    [
        tf.keras.Input(shape=(400,)),
        Dense(units=25,activation='relu',name='l1'),
        Dense(units=15,activation='relu',name='l2'),
        Dense(units=10,activation='linear',name='l3')
    ], name = "my_model"
)

model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=['accuracy']
)

history = model.fit(
    X,y,
    epochs=10
)

# print(history.history['loss'])

# plot_loss_tf(history)

# image_of_two = X[1015]
# display_digit(image_of_two,y)
m, n = X.shape
fig,axes = plt.subplots(8,8,figsize=(5,5))
fig.tight_layout(pad=0.13,rect=[0, 0.03, 1, 0.91]) #[left, bottom, right, top]
widgvis(fig)

for i,ax in enumerate(axes.flat):
    random_index = np.random.randint(m)
    X_random_reshaped = X[random_index].reshape((20, 20)).T
    # Display the image
    ax.imshow(X_random_reshaped, cmap='gray')
    prediction = model.predict(X[random_index].reshape(1,-1))

    prediction = tf.nn.softmax(prediction)
    prediction = np.argmax(prediction)

    ax.set_title(f'{y[random_index,0]},{prediction}',fontsize=10)
    ax.set_axis_off()
fig.suptitle("Label, yhat", fontsize=14)
print( f"{display_errors(model,X,y)} errors out of {len(X)} images")
print(prediction)
# print(model.info)
# weights, biases = model.layers[-1].get_weights()
# print("Weights:", weights)  # 打印最后一层的权重
# print("Biases:", biases)
plt.show()