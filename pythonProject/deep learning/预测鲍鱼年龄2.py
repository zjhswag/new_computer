import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

# 数据加载和初步探索
column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
data = pd.read_csv('abalone.data', names=column_names)

# 数据预处理
# 将类别特征 'Sex' 转换为独热编码
data = pd.get_dummies(data, columns=['Sex'])
print(data.head())
# 分离特征和目标变量
X = data.drop('Rings', axis=1)
y = data['Rings']

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_test.describe())
# 创建一个包含预处理和模型的管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # 特征标准化
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))  # 随机森林回归器
])

# 训练模型
pipeline.fit(X_train, y_train)
print(X_test.shape)
# 模型评估
y_pred = pipeline.predict(X_test)

y1 = pipeline.predict(X[:100])
print("result vs predict",y1,'\n',y[:100])

r_squared = pipeline.score(X_test, y_test)
print(f"R² Score: {r_squared}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

X_test= np.array(X_test)
y_test= np.array(y_test)

# print(y_test)

print('max is',np.max(y_pred),'min is',np.min(y_pred))
# print(tey)
# plt.subplot(1,2,1)
plt.scatter(X_test[:,0],y_test,marker='o', c='y')
# plt.subplot(1,2,2)
plt.scatter(X_test[:,0],y_pred,marker='x', c='r')
plt.show()
# 可以使用 pipeline.predict(some_data) 来进行新的预测
