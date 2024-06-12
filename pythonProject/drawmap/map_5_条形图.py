import matplotlib.pyplot as plt
import numpy as np
import math

data = [[30, 25, 50, 20],
        [40, 23, 51, 17],
        [35, 22, 45, 19]]
X = np.arange(4)
# print(X)
fig,ax = plt.subplots(1,1,figsize=(10,4))
ax.bar(X, data[0], color='b', width=0.25)          # 0,1,2,3 对应着不同的data值
ax.bar(X + 0.25, data[1], color='g', width=0.25)
ax.bar(X + 0.50, data[2], color='r', width=0.25)
plt.show()