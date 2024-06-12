import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import cross_val_score  # 交叉验证
import seaborn as sns
from sklearn.model_selection import train_test_split
pd.set_option('display.max_rows', 100)  # 例如显示最多 100 行
pd.set_option('display.max_columns', 50)
column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
data = pd.read_csv('abalone.data', names=column_names, delimiter=',')

data["Rings"] = data['Rings'] + 1.5

# data = np.genfromtxt('abalone.data', names=column_names, delimiter=',',skip_header=0)

# 使用 Seaborn 绘制箱形图
# sns.countplot(x='Sex',data=data)
# data['Sex'].value_counts()
# plt.show()

# 展示数据
# print(data)
# print(data.head())
# print(data.shape)
# print(data.info())
print(data.describe()) # 平均值，max,特征等，方差，min

# I,0.11,0.09,0.03,0.008,0.0025,0.002,0.003,3
# i=1
# plt.figure(figsize=(16,8))
# for col in data.columns[1:]:
#     plt.subplot(4,2,i)
#     i=i+1
#     sns.distplot(data[col])
# plt.tight_layout()

# 连续特征之间的散点图


# 展示各个特征之间的关系
# sns.pairplot(data,hue='Sex')
# plt.show()

# 计算特征之间的相关系数矩阵
# corr_df = data.corr()
# print(corr_df)

# 独热编码 'Sex' 列
# 将独热编码的列与原始数据集合并
#
sex_dummies = pd.get_dummies(data['Sex'], prefix='Sex')
data = pd.concat([data, sex_dummies], axis=1)

# 删除原始的 'Sex' 列
data.drop('Sex', axis=1, inplace=True)
# data['ones'] = 1
# 提取特征和目标变量
x = data.drop('Rings', axis=1)
y = data['Rings']
# print(x,y)
# 注意这里的x,y为panda数
x = np.array(x)
y = np.array(y)
# 如果性别只包含两个用这个方法：
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # for i in range(len(x[:])):
# #     if x[i, 0] == 'M':
# #         x[i, 0] = 0
# #     else:
# #         x[i, 0] = 1

# x[:, 0] = np.where(x[:, 0] == 'M', 0, 1)  # 上面循环的代替，高效，将m换成0，然后才能再归一化处理

# 标准化特征
# scaler = StandardScaler()
# X_norm = scaler.fit_transform(x)
# print(X_norm)

# print(f"Peak to Peak range by column in Raw        X:{np.ptp(x, axis=0)}")
# print(f"Peak to Peak range by column in Normalized X:{np.ptp(X_norm, axis=0)}")

# 方法一
# sgdr = SGDRegressor(max_iter=1000, average=True)
# sgdr.fit(X_norm, y)
# print(
#     f"number of iterations completed: {sgdr.n_iter_}, number of weight updates: {sgdr.t_}, 模型评分：{sgdr.score(X_norm, y)}")
#
# b_norm = sgdr.intercept_  # 获取截距
# w_norm = sgdr.coef_  # 获取特征权重
# print(f"model parameters:                   w: {w_norm}, b:{b_norm}")

# 方法二
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
b = linear_model.intercept_
w = linear_model.coef_
print(f"w= {w}, b={b}")
y_pred = linear_model.predict(X_test)
y1 = linear_model.predict(x[:2])
print(y1,y[:2])
# scores = cross_val_score(linear_model, X_test, y_test, cv=5)  # cv 是折叠数
# print("Cross-validated scores:", scores)

r_squared = linear_model.score( X_test, y_test)
print("R² score:", r_squared)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
plt.scatter(X_test[:,1],y_test,marker='o', c='y')
plt.scatter(X_test[:,1],y_pred,marker='x', c='r')
plt.show()


# y_pred = np.dot(X_norm, w_norm) + b_norm
#
# fig, ax = plt.subplots(1, 7, figsize=(12, 10), sharey=True)
# for i in range(7):
#     ax[i].scatter(x[:, i], y, color="b", label='target')
#     ax[i].set_xlabel(column_names[i+1])
#     # ax[i].scatter(x[:, i], y_pred, color='r', label='predict')
# ax[0].set_ylabel("Price");
# ax[0].legend();
# fig.suptitle("target versus prediction using z-score normalized model")
# plt.show()
# X_norm = scaler_X.fit_transform(X)
# X_norm = np.concatenate((X_norm, intercept), axis=1)
# plt.subplot(1,2,1)
# plt.scatter(x[:,1],y)
# plt.subplot(1,2,2)
# plt.scatter(X_norm[:,1],y)
# plt.show()
# print(X_original,'\n', X_norm)
