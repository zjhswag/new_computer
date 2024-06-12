# Plot the decision boundary for a logistic regression model.
# This will give you a better sense of what the model is predicting
# 决策边界，注意调用的sigmoid函数和draw_thresh

import numpy as np
import matplotlib.pyplot as plt
from lab_utils_common import plot_data, sigmoid, draw_vthresh

plt.style.use('./deeplearning.mplstyle')

X = np.array([[0.5, 1.5], [1, 1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y = np.array([0, 0, 0, 1, 1, 1]).reshape(-1, 1)
#
#
# fig, ax = plt.subplots(1,1,figsize=(5.5, 4))
# plot_data(X, y, ax)
# ax.axis([0, 4, 0, 3.5])
# ax.set_ylabel('$x_1$')
# ax.set_xlabel('$x_0$')
# plt.show()
# 展示分界

# Plot sigmoid(z) over a range of values from -10 to 10
# z = np.arange(-10,11)
#
# fig,ax = plt.subplots(1,1,figsize=(5,3))
# # Plot z vs sigmoid(z)
# ax.plot(z, sigmoid(z), c="b")
#
# ax.set_title("Sigmoid function")
# ax.set_ylabel('sigmoid(z)')
# ax.set_xlabel('z')
# draw_vthresh(ax,0)
# plt.show()
# 展示sigmoid函数

# As you can see,  𝑔(𝑧)>=0.5 for  𝑧>=0 predict y =1

# Choose values between 0 and 6
x0 = np.arange(0,6)
# print(x0)
x1 = 3 - x0
# print(x0,x1)
# plt.plot(x0, x1)
fig,ax = plt.subplots(1,1,figsize=(6,4))
# Plot the decision boundary
ax.plot(x0,x1, c="b")
ax.axis([0, 4, -1, 3.5])

# Fill the region below the line
ax.fill_between(x0,x1, alpha=0.2)

# Plot the original data
plot_data(X,y,ax)
ax.set_ylabel('$x_1$')
ax.set_xlabel('$x_0$')
plt.show()

# 蓝色的分界线为决策边界