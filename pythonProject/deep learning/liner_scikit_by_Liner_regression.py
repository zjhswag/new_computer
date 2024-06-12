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

# load the dataset
X_train, y_train = load_house_data()
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

b = linear_model.intercept_
w = linear_model.coef_
print(f"w= {w}, b={b}")
from sklearn.model_selection import cross_val_score
scores = cross_val_score(linear_model, X_train, y_train, cv=5)  # cv 是折叠数
print("Cross-validated scores:", scores)
r_squared = linear_model.score(X_train, y_train)
print("R² score:", r_squared)

x_house = np.array([1200, 3,1, 40]).reshape(-1,4)
x_house_predict = linear_model.predict(x_house)[0]  # 没有这个【0】,就不能使用后面的.2f,返回的是一个numpy.array类型，不是一个数值
print(x_house_predict, type(linear_model.predict(x_house)))
print(f" predicted price of a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old = ${x_house_predict*1000:0.2f}")

# 虽然，使用随机梯度下降估计参数的方法SGDRegression（使用梯度下降法，需要进行特征工程）在性能表现上不及使用解析方法的LinerRegression(使用解方程的方法)；
# 但是如果面对训练数据规模十分庞大的任务，随机梯度法不论是在分类还是回归问题上都表现得十分高效，
# 可以在不损失过多性能的前提下，节省大量计算时间。参考Sklearn官网的建议，如果数据规模超过10万，推荐使用随机梯度法估计参数模型。
