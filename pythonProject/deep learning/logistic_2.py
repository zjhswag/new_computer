# explore the sigmoid function (also known as the logistic function)
# explore logistic regression; which uses the sigmoid function
import numpy as np
import matplotlib.pyplot as plt
from plt_one_addpt_onclick import plt_one_addpt_onclick
from lab_utils_common import draw_vthresh
plt.style.use('./deeplearning.mplstyle')

# Input is an array.
input_array = np.arange(1,4)
exp_array = np.exp(input_array)

print("Input to exp:", input_array)
print("Output of exp:", exp_array)
# print(np.c_[input_array, exp_array])
# Input is a single number
input_val = 1
exp_val = np.exp(input_val)
# print(2.73**2)
print("Input to exp:", input_val)
print("Output of exp:", exp_val)


def sigmoid(z):
    """
    Compute the sigmoid of z

    Args:
        z (ndarray): A scalar, numpy array of any size.

    Returns:
        g (ndarray): sigmoid(z), with the same shape as z

    """

    g = 1 / (1 + np.exp(-z))

    return g


z_tmp = np.arange(-10,11)
print(z_tmp)
# Use the function implemented above to get the sigmoid values
y = sigmoid(z_tmp)

# Code for pretty printing the two arrays next to each other
np.set_printoptions(precision=3)
print("Input (z), Output (sigmoid(z))")
print(np.c_[z_tmp, y])

# Plot z vs sigmoid(z)
fig,ax = plt.subplots(1,1,figsize=(5,3))
ax.plot(z_tmp, y, c="b")
ax.set_title("Sigmoid function")
ax.set_ylabel('sigmoid(z)')
ax.set_xlabel('z')
draw_vthresh(ax,0)

# plt.plot(z_tmp, y, c="b")
# plt.title("Sigmoid function")
# plt.ylabel('sigmoid(z)')
# plt.xlabel('z')
# plt.show()
x_train = np.array([0., 1, 2, 3, 4, 5])
y_train = np.array([0,  0, 0, 1, 1, 1])

w_in = np.zeros((1))
b_in = 0
addpt = plt_one_addpt_onclick( x_train,y_train, w_in, b_in, logistic=True)
plt.show()