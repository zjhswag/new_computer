# implement linear regression with one variable to predict profits for a restaurant franchise.
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from utils_slide import *
import math
from sklearn.metrics import mean_squared_error, r2_score
mpl.rcParams['font.sans-serif'] = ['KaiTi']
x_train, y_train = load_data()


# print x_train
print("Type of x_train:", type(x_train))
# print("First five elements of x_train are:\n", x_train[:5])


plt.scatter(x_train, y_train, marker='X', c='r', label="数据分析")
plt.xlabel('Profit in $10,000')
plt.ylabel('Population of City in 10,000s')
plt.legend()
plt.title("Profits vs. Population per city")
plt.show()


def compute_cost(w, b, X_train, Y_train):
    cost = 0
    n = X_train.shape[0]
    for i in range(n):
        cost += ((X_train[i] * w) + b - Y_train[i]) ** 2
    return cost / (2 * n)


# Compute cost with some initial values for paramaters w, b
# initial_w = 2
# initial_b = 1
#
# cost = compute_cost(initial_w, initial_b, x_train, y_train)


# print(cost)
# print(f'Cost at initial w (zeros): {cost:.3f}')


def compute_gradient(x, y, w, b):
    n = x.shape[0]
    db = 0
    dw = 0
    for i in range(n):
        db += (x[i] * w + b) - y[i]
        dw += ((x[i] * w + b) - y[i]) * x[i]
    return dw / n, db / n


# initial_w = 0
# initial_b = 0
# 验证函数准确性
# tmp_dj_dw, tmp_dj_db = compute_gradient(x_train, y_train, initial_w, initial_b)
# print('Gradient at initial w, b (zeros):', tmp_dj_dw, tmp_dj_db)


def gradient_descent(x, y, win, bin, cost_f, gradient_f, alpha, iters):
    n = x.shape[0]
    j_hist = []
    d_hist = []
    b = bin
    w = win
    for i in range(iters):
        dw, db = gradient_f(x, y, w, b)
        # print(w)
        w = w - alpha * dw
        b = b - alpha * db
        if i % 100 == 0:
            d_hist.append([w, b])
        j_hist.append(cost_f(w, b, x, y))
    return w, b, d_hist, j_hist


# 程序开端
# 通过梯度下降,计算w和b的值
initial_w = 0.
initial_b = 0.

# some gradient descent settings
iterations = 1500
alpha = 0.01

w1, b1, d_history, j_history = gradient_descent(x_train, y_train, initial_w, initial_b,
                                                compute_cost, compute_gradient, alpha, iterations)
# 输出计算得到的数据
print("w,b found by gradient descent:", w1, b1)

for i in range(math.ceil(iterations / 100)):
    print(d_history[i])

print(j_history[0], j_history[-1])

# 计算预测数据用来绘制预测曲线
m = x_train.shape[0]
predicted = np.zeros(m)
for i in range(m):
    predicted[i] = w1 * x_train[i] + b1

# 计算 MSE
mse = mean_squared_error(y_train, predicted)

# 计算 RMSE
rmse = np.sqrt(mse)

# 计算 R² Score
r2 = r2_score(y_train, predicted)

print("均方误差 (MSE):", mse)
print("均方根误差 (RMSE):", rmse)
print("决定系数 (R² Score):", r2)

plt.plot(x_train, predicted, c='b')
# 可以描线，也可以绘点
# plt.scatter(x_train, predicted, marker='o', c='y')
plt.scatter(x_train, y_train, marker='x', c='r')

plt.title("Profits vs. Population per city")
plt.ylabel('Profit in $10,000')
plt.xlabel('Population of City in 10,000s')

# 验证数据正确
# predict1 = 3.5 * w1 + b1
# print('For population = 35,000, we predict a profit of $%.2f' % (predict1*10000))
#
# predict2 = 7.0 * w1 + b1
# print('For population = 70,000, we predict a profit of $%.2f' % (predict2*10000))


plt.show()
