import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)

x1 = np.random.rand(100, 1)
x2 = np.random.rand(100, 1)
# print(x1)
noise = np.random.normal(0, 1, (100, 1))
# print(noise)
y = 100 * x1 + 10 * x2 + 3 + noise
X = np.hstack([x1, x2, np.ones((100, 1))])
# print(X)

X[:, 1] *= 1000  # 第一个特征
X[:, 2] *= 0.001  # 第二个特征
# print(X)
model = LinearRegression()

model.fit(X, y)

# 输出模型参数
print("Weights: ", ['%.5f' % elem for elem in model.coef_[0]])
print("Bias: %.5f" % model.intercept_)

X_scaled = np.copy(X)
# print(X_scaled)
for i in range(X_scaled.shape[1]):
    if np.max(X_scaled[:, i]) != np.min(X_scaled[:, i]):
        X_scaled[:, i] = (X_scaled[:, i] - np.min(X_scaled[:, i])) / (np.max(X_scaled[:, i]) - np.min(X_scaled[:, i]))

model.fit(X_scaled, y)

# 输出模型参数
print("Weights after scaling: ", ['%.5f' % elem for elem in model.coef_[0]])
print("Bias after scaling: %.5f" % model.intercept_)