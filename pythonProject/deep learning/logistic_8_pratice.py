import numpy as np
import matplotlib.pyplot as plt
from utils import *
import copy
import math
# 根据学生的两科成绩预测学生是否被录取
# X_train,y_train = load_data("ex2data1.txt")
# print(X_train[:2])
# print(X_train.shape)
# print(np.sum(y_train == 1)) # 60个
from lab_coffee_utils import load_coffee_data, plt_roast, plt_prob, plt_layer, plt_network, plt_output_unit
X_train,y_train = load_coffee_data()
print(X_train[0],y_train[0])
print(X_train[:2])
print(X_train.shape,y_train.shape)
# Y = y_train.reshape(-1,)
plot_data(X_train, y_train, pos_label="Admitted1", neg_label="Not admitted")

plt.ylabel('Exam 2 score')
# Set the x-axis label
plt.xlabel('Exam 1 score')
plt.legend(loc="lower left")

plt.show()

def sigmoid(z):
    g = 1/(1+np.exp(-z))
    return g


def compute_cost(X, y, w, b, lambda_=None):
    """
    Computes the cost over all examples
    Args:
      X : (ndarray Shape (m,n)) data, m examples by n features
      y : (array_like Shape (m,)) target value
      w : (array_like Shape (n,)) Values of parameters of the model
      b : scalar Values of bias parameter of the model
      lambda_: unused placeholder
    Returns:
      total_cost: (scalar)         cost
    """

    m, n = X.shape
    cost = 0
    for i in range(m):
        z_1 = np.dot(X[i], w)+b
        g = sigmoid(z_1)
        cost += -y[i]*np.log(g)-(1-y[i])*np.log(1-g)
    return cost/m


def compute_gradient(X, y, w, b, lambda_=None):
    """
    Computes the gradient for logistic regression

    Args:
      X : (ndarray Shape (m,n)) variable such as house size
      y : (array_like Shape (m,1)) actual value
      w : (array_like Shape (n,1)) values of parameters of the model
      b : (scalar)                 value of parameter of the model
      lambda_: unused placeholder.
    Returns
      dj_dw: (array_like Shape (n,1)) The gradient of the cost w.r.t. the parameters w.
      dj_db: (scalar)                The gradient of the cost w.r.t. the parameter b.
    """
    m, n = X.shape
    dj_dw = np.zeros(w.shape)
    dj_db = 0.
    for i in range(m):
        z_1 = np.dot(X[i], w)+b
        g = sigmoid(z_1)
        dj_db += g-y[i]
        for j in range(n):
            dj_dw[j] +=(g-y[i])*X[i][j]
    dj_db /= m
    dj_dw /= m
    return dj_db, dj_dw


def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters, lambda_):
    m = len(X)

    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    w_history = []

    for i in range(num_iters):

        # Calculate the gradient and update the parameters
        dj_db, dj_dw = gradient_function(X, y, w_in, b_in, lambda_)

        # Update Parameters using w, b, alpha and gradient
        w_in = w_in - alpha * dj_dw
        b_in = b_in - alpha * dj_db

        # Save cost J at each iteration
        if i < 100000:  # prevent resource exhaustion
            cost = cost_function(X, y, w_in, b_in, lambda_)
            J_history.append(cost)

        # Print cost every at intervals 10 times or as many iterations if < 10
        if i % math.ceil(num_iters / 10) == 0 or i == (num_iters - 1):
            w_history.append(w_in)
            print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.8f}   ")

    return w_in, b_in, J_history, w_history  # return w and J,w history for graphing





def predict(X, w, b):
    """
    Predict whether the label is 0 or 1 using learned logistic
    regression parameters w
    Args:
    X : (ndarray Shape (m, n))
    w : (array_like Shape (n,))      Parameters of the model
    b : (scalar, float)              Parameter of the model
    Returns:
    p: (ndarray (m,1))
        The predictions for X using a threshold at 0.5
    """
    m, n = X.shape
    p = np.zeros(m)
    for i in range(m):
        z1 = np.dot(X[i],w)+b
        g = sigmoid(z1)
        if g > 0.5:
            p[i] = 1
        else:
            p[i] = 0
    return p

np.random.seed(1)
initial_w = 0.01 * (np.random.rand(2).reshape(-1,1) - 0.5)
# print(initial_w)
initial_b = -8


# Some gradient descent settings
iterations = 10000
alpha = 0.001

w,b, J_history,_ = gradient_descent(X_train ,y_train, initial_w, initial_b,
                                   compute_cost, compute_gradient, alpha, iterations, 0)
print(w, b)

# 根据本数据集看模型预测效果
# pre_y = predict(X_train,w,b)
#
# positive = pre_y == 1
# negative = pre_y == 0
#
# # Plot examples
# plt.plot(X_train[positive, 0], X_train[positive, 1], 'bh',label='pp')
# plt.plot(X_train[negative, 0], X_train[negative, 1], 'rd',label='pn')
# plt.legend(loc="lower right")
# plot_decision_boundary(w, b, X_train, y_train)
# p = predict(X_train, w,b)
# print('Train Accuracy: %f'%(np.mean(p == y_train) * 100))

# plt.show()
