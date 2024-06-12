import matplotlib.pyplot as plt

import numpy as np
X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
print(type(X_train))
# x = np.linspace(0.05, 10, 1000)
#
# y = np.random.rand(1000)
#
# plt.scatter(x, y, label="scatter figure")
# #
# # plt.legend()
# print(5.5e-01-(9.9e-7*6.4e+05))
# # plt.show()
# print(np.ceil(100 / 10000))

y1 = np.random.rand(4,4)
print(type(y1))  # <class 'numpy.ndarray'>
# y2 = y1.I      # 导致报错 AttributeError: 'numpy.ndarray' object has no attribute 'I'
# print(y1*y2)
print(y1)
x1 = np.mat(np.random.rand(4,4))
print(type(x1))  # <class 'numpy.matrix'>
print(x1)
x2 =x1.I
x3 = x2*x1
print(x3)





# 样本数据
# data = [1, 2, 3, 1, 4, 2, 3, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 2, 3, 4]
#
# # 绘制直方图
# plt.hist(data, bins=6, edgecolor='black')
#
# # 添加标签和标题
# # plt.xlabel('数值')
# # plt.ylabel('频率')
# # plt.title('直方图')
#
# # 显示直方图
# plt.show()