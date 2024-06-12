import matplotlib.pyplot as plt
import numpy as np
import math

# 显示中文设置...
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False  # 步骤二(解决坐标轴负数的负号显示问题)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
x = np.arange(1, 5)
axes[0].plot(x, np.exp(x))
axes[0].plot(x, x ** 2)
axes[0].set_title("正常比例")
axes[1].plot(x, np.exp(x))
axes[1].plot(x, x ** 2)
axes[1].set_yscale("log")  # 主要是这个
axes[1].set_title("对数刻度(y)")
axes[0].set_xlabel("x 轴")
axes[0].set_ylabel("y 轴")
axes[0].xaxis.labelpad = 10
axes[1].set_xlabel("x 轴")
axes[1].set_ylabel("y 轴")

plt.show()