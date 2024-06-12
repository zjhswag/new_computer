import numpy as np

np.set_printoptions(precision=2)
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.preprocessing import StandardScaler
from lab_utils_multi import load_house_data
import matplotlib.pyplot as plt

dlblue = '#0096ff';
dlorange = '#FF9300';
dldarkred = '#C00000';
dlmagenta = '#FF40FF';
dlpurple = '#7030A0';
plt.style.use('./deeplearning.mplstyle')

X_train, y_train = load_house_data()
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']

scaler = StandardScaler()
X_norm = scaler.fit_transform(X_train)
print(f"Peak to Peak range by column in Raw        X:{np.ptp(X_train, axis=0)}")
print(f"Peak to Peak range by column in Normalized X:{np.ptp(X_norm, axis=0)}")

sgdr = SGDRegressor(max_iter=1000, average=True)
sgdr.fit(X_norm, y_train)

print(f"number of iterations completed: {sgdr.n_iter_}, number of weight updates: {sgdr.t_}, 模型评分：{sgdr.score(X_norm, y_train)}")

b_norm = sgdr.intercept_  # 获取截距
w_norm = sgdr.coef_  # 获取特征权重
print(f"model parameters:                   w: {w_norm}, b:{b_norm}")
print(f"model parameters from previous lab: w: [110.56 -21.27 -32.71 -37.97], b: 363.16")

# make a prediction using sgdr.predict()
# y_pred_sgd = sgdr.predict(X_norm)  # 证明predict和正常方法一样
# print(y_pred_sgd[:4])
# # make a prediction using w,b.
y_pred = np.dot(X_norm, w_norm) + b_norm
# print(f"prediction using np.dot() and sgdr.predict match: {(y_pred == y_pred_sgd).all()}")

# print(f"Prediction on training set:\n{y_pred[:4]}")
# print(f"Target values \n{y_train[:4]}")

#
# plot predictions and targets vs original features
fig, ax = plt.subplots(1, 4, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:, i], y_train, color="b", label='target')
    ax[i].set_xlabel(X_features[i])
    ax[i].scatter(X_train[:, i], y_pred, color=dlorange, label='predict')
ax[0].set_ylabel("Price");
ax[0].legend();
fig.suptitle("target versus prediction using z-score normalized model")
plt.show()

# 对比之前的improve2，可以发现skit库更厉害，
