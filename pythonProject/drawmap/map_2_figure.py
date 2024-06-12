import matplotlib.pyplot as plt

# 显示中文设置...
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一(替换sans-serif字体)
plt.rcParams['axes.unicode_minus'] = False  # 步骤二(解决坐标轴负数的负号显示问题)

y = [1, 4, 9, 16, 25, 36, 49, 64]
x1 = [1, 16, 30, 42, 55, 68, 77, 88]
x2 = [1, 6, 12, 18, 28, 40, 52, 65]
fig,(ax,ax1) = plt.subplots(1, 2, figsize=(5, 4))

l1 = ax.plot(x1, y, 'ys-')  # solid line with yellow colour and square marker
l2 = ax1.plot(x2, y, 'go--')  # dash line with green colour and circle marker
ax.legend(labels=('电视', '智能手机'), loc='center')  # legend placed at lower right
ax.set_title(u"广告对销售的影响")
ax.set_xlabel('媒介')
ax.set_ylabel('销售')

plt.show()