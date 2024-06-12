import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1,1,figsize=(10,5))
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])

# ax.hist(a, bins=[0,25, 50, 75, 100]) # 这个参数定义了直方图的分桶（bin）边界。
# 在这个例子中，数据将被分成四个桶,每个桶将计算其范围内的数值数量，并在直方图上相应地显示这个数量。

n, bins, patches = ax.hist(a, bins=[0, 25, 50, 75, 100])
# 在每个柱状图上方添加数量标签
for bin_edge, count in zip(bins, n):
    print(count)
    ax.text(bin_edge + 12.5,  count,str(int(count)), ha='center', va='bottom')  # 前两个参数设置xy

ax.set_title("结果直方图")
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel('分数')
ax.set_ylabel('学生数量')
plt.show()