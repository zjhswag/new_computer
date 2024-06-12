# explore the reason the squared error loss is not appropriate for logistic regression
# explore the logistic loss function
# 确定平方误差损失函数不适合分类任务
# 开发并研究了适用于分类任务的 logistic 损失函数。

import numpy as np
import matplotlib.pyplot as plt

from plt_logistic_loss import plt_logistic_cost, plt_two_logistic_loss_curves, plt_simple_example
from plt_logistic_loss import soup_bowl

soup_bowl()

x_train = np.array([0., 1, 2, 3, 4, 5], dtype=np.longdouble)
y_train = np.array([0, 0, 0, 1, 1, 1], dtype=np.longdouble)
# plt_simple_example(x_train, y_train)
# print(np.log(0.0000008))
# plt_two_logistic_loss_curves()
cst = plt_logistic_cost(x_train,y_train)
plt.show()
