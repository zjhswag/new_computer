import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False  # 步骤二(解决坐标轴负数的负号显示问题)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
x = np.arange(1, 11)
axes[0].plot(x, x ** 3, 'g', lw=2)
axes[0].grid(True)
axes[0].set_title('默认网格')
print(np.exp(2))
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='b', ls='-.', lw=1)
axes[1].set_title('自定义网格')
axes[2].plot(x, x)
axes[2].set_title('无网格')
fig.tight_layout()
plt.show()
