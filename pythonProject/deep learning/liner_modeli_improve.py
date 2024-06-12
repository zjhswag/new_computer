import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

dlblue = '#0096ff';
dlorange = '#FF9300';
dldarkred = '#C00000';
dlmagenta = '#FF40FF';
dlpurple = '#7030A0';
from lab_utils_multi import load_house_data, compute_cost, run_gradient_descent
from lab_utils_multi import norm_plot, plt_contour_multi, plt_equal_scale, plot_cost_i_w

X_train, y_train = load_house_data()
# print(len(X_train))
# print(X_train)
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']

# 展示各个特征数据和target之间的关系
# fig, ax = plt.subplots(1, 4, figsize=(12, 6), sharey=True)
# for i in range(len(ax)):
#     ax[i].scatter(X_train[:, i], y_train, label="House price")
#     ax[i].set_xlabel(X_features[i])
# ax[0].set_ylabel("Price (1000's)")
# plt.legend()
# plt.show()

# 未使用特征缩放的梯度下降
W1, b1, hist = run_gradient_descent(X_train, y_train, 1000, alpha=9e-7)
m = X_train.shape[0]
yp = np.zeros(m)
for i in range(m):
    yp[i] = np.dot(X_train[i], W1) + b1

    # plot predictions and targets versus original features
fig,ax=plt.subplots(1,4,figsize=(12, 3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],y_train, label = 'target')
    ax[i].set_xlabel(X_features[i])
    ax[i].scatter(X_train[:,i],yp,color=dlorange, label = 'predict')
ax[0].set_ylabel("Price"); ax[0].legend();
fig.suptitle("target versus prediction without using z-score normalized model")
x_house = np.array([1200, 3, 1, 40])
print(f"未使用归一化进行预测的值为{(x_house.dot(W1)+b1)*1000:0.2f}")

# plot_cost_i_w(X_train, y_train, hist)


def zscore_normalize_features(X):
    """
    computes  X, zcore normalized by column

    Args:
      X (ndarray): Shape (m,n) input data, m examples, n features

    Returns:
      X_norm (ndarray): Shape (m,n)  input normalized by column
      mu (ndarray):     Shape (n,)   mean of each feature
      sigma (ndarray):  Shape (n,)   standard deviation of each feature
    """
    # find the mean of each column/feature
    mu = np.mean(X, axis=0)  # mu will have shape (n,)
    # find the standard deviation of each column/feature
    sigma = np.std(X, axis=0)  # sigma will have shape (n,)
    # element-wise, subtract mu for that column from each example, divide by std for that column
    X_norm = (X - mu) / sigma

    return (X_norm, mu, sigma)


# 比较对特征进行缩放的效果

# mu = np.mean(X_train, axis=0)
# sigma = np.std(X_train, axis=0)  # axis = 0 表示对列操作
# X_mean = (X_train - mu)
# X_norm = (X_train - mu) / sigma
#
# fig, ax = plt.subplots(1, 3, figsize=(12, 3))
# ax[0].scatter(X_train[:, 0], X_train[:, 3])
# ax[0].set_xlabel(X_features[0]);
# ax[0].set_ylabel(X_features[3]);
# ax[0].set_title("unnormalized")
# ax[0].axis('equal')
#
# ax[1].scatter(X_mean[:, 0], X_mean[:, 3])
# ax[1].set_xlabel(X_features[0]);
# ax[0].set_ylabel(X_features[3]);
# ax[1].set_title(r"X - $\mu$")
# ax[1].axis('equal')
#
# ax[2].scatter(X_norm[:, 0], X_norm[:, 3])
# ax[2].set_xlabel(X_features[0]);
# ax[0].set_ylabel(X_features[3]);
# ax[2].set_title(r"Z-score normalized")
# ax[2].axis('equal')
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 自动调整子图参数，使之填充整个图像区域
# fig.suptitle("distribution of features before, during, after normalization")

# print(mu, sigma) # [1.42e+03 2.72e+00 1.38e+00 3.84e+01] [411.62   0.65   0.49  25.78]
# print(X_mean[:3])
# print(X_norm[:3])
X_norm, X_mu, X_sigma = zscore_normalize_features(X_train)
print(f"X_mu = {X_mu}, \nX_sigma = {X_sigma}")
# print(f"Peak to Peak range by column in Raw        X:{np.ptp(X_train,axis=0)}")  # 每一列的最大值和最小值之间的差值X:[2.41e+03 4.00e+00 1.00e+00 9.50e+01]
# print(f"Peak to Peak range by column in Normalized X:{np.ptp(X_norm,axis=0)}")   # 每一列的最大值和最小值之间的差值X:[5.85 6.14 2.06 3.69]
# plt.show()


# 展示缩放特征之后 数据的变化
# fig, ax = plt.subplots(1, 4, figsize=(12, 3))
# for i in range(len(ax)):
#     norm_plot(ax[i], X_train[:, i], )
#     ax[i].set_xlabel(X_features[i])
# ax[0].set_ylabel("count");
# fig.suptitle("distribution of features before normalization")
# fig, ax = plt.subplots(1, 4, figsize=(12, 4))
# for i in range(len(ax)):
#     norm_plot(ax[i], X_norm[:, i], )
#     ax[i].set_xlabel(X_features[i])
# ax[0].set_ylabel("count");
# fig.suptitle(f"distribution of features after normalization")
# plt.show()


w_norm, b_norm, hist = run_gradient_descent(X_norm, y_train, 1000, 1.0e-1, )
# predict target using normalized features使用归一化的数据来进行预测
m = X_norm.shape[0]
yp = np.zeros(m)
for i in range(m):
    yp[i] = np.dot(X_norm[i], w_norm) + b_norm

    # plot predictions and targets versus original features
fig,ax=plt.subplots(1,4,figsize=(12, 3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],y_train, label = 'target')
    ax[i].set_xlabel(X_features[i])
    ax[i].scatter(X_train[:,i],yp,color=dlorange, label = 'predict')
ax[0].set_ylabel("Price"); ax[0].legend();
fig.suptitle("target versus prediction using z-score normalized model")


# First, normalize out example.
x_house = np.array([1200, 3, 1, 40])
x_house_norm = (x_house - X_mu) / X_sigma  # 利用归一化模型来预测一个房价，必须使用训练数据归一化时得出的平均值和标准差对数据进行归一化。
# print(x_house_norm)
x_house_predict = np.dot(x_house_norm, w_norm) + b_norm
print(f" predicted price of a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old = ${x_house_predict*1000:0.0f}")
plt_equal_scale(X_train, X_norm, y_train)
plt.show()
