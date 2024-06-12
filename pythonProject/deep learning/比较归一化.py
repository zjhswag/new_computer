import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
np.random.seed(0)
data = np.random.randint(0, 100, 50)

# 进行0-1标准化
data_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

# 打印最小值和最大值，验证性质1
print(f"Min: {data_normalized.min()}, Max: {data_normalized.max()}")

# 生成一个值来验证性质2
value1 = data[10]
value2 = data[20]
normalized_value1 = data_normalized[10]
normalized_value2 = data_normalized[20]
print(f"Original: {value1} > {value2} --> Normalized: {normalized_value1} > {normalized_value2}")

# 添加一个极端值来验证性质3
data_with_outlier = np.append(data, 1000)
data_with_outlier_normalized = (data_with_outlier - np.min(data_with_outlier)) / (np.max(data_with_outlier) - np.min(data_with_outlier))

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data_normalized, bins=20)
plt.title("Without Outlier")
plt.subplot(1, 2, 2)
plt.hist(data_with_outlier_normalized, bins=20)
plt.title("With Outlier")
# plt.show()

# 画图来验证性质4
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data, bins=20)
plt.title("Original Data")
plt.subplot(1, 2, 2)
plt.hist(data_normalized, bins=20)
plt.title("Normalized Data")
# plt.subplot(2, 2, 3)
# plt.hist(data, bins=20)
# plt.title("Original Data")
# plt.subplot(2, 2, 4)
# plt.hist(data_normalized, bins=20)
# plt.title("Normalized Data")
plt.show()