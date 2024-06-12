import math

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False  # 步骤二(解决坐标轴负数的负号显示问题)
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

# print(x,y)

plt.plot(x,y, 'b^')
# 符号：^ , v , < , > , s , + , x , D , d , 1 , 2 , 3 , 4 , h , H , p , | , _ , - , –, -., , . , , , o ,
# 颜色：b, g, r, c, m, y, k, w
plt.xlabel(u"角度")
plt.ylabel("正弦")
plt.title('正弦波')
plt.show()

