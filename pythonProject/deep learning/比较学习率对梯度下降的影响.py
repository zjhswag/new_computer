import numpy as np
import matplotlib.pyplot as plt

# 设置随机数种子
np.random.seed(42)

def convex_function(x):
    return x**2

def gradient_descent(initial_x, learning_rate, num_iterations):
    x_values = [initial_x]  # 用于存储每次迭代的x值
    y_values = [convex_function(initial_x)]  # 用于存储每次迭代的函数值

    x = initial_x

    for i in range(num_iterations):
        gradient = 2 * x  # 函数 f(x) = x^2 的导数为 f'(x) = 2x
        x -= learning_rate * gradient

        x_values.append(x)
        y_values.append(convex_function(x))

    return x_values, y_values

# 参数设置
initial_x = 4  # 初始值
learning_rates = [0.01, 1.01]  # 学习率
num_iterations = 20

# 生成凸函数的数据
x = np.linspace(-6, 6, 200)  # 生成 x 值
y = convex_function(x)  # 凸函数 f(x) = x^2

# 绘制两个子图
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 针对每个学习率进行绘制
for i, learning_rate in enumerate(learning_rates):
    # 运行梯度下降算法
    x_values, y_values = gradient_descent(initial_x, learning_rate, num_iterations)

    # 绘制凸函数的曲线
    axs[i].plot(x, y, label="Convex Function")

    # 绘制梯度下降轨迹
    axs[i].plot(x_values, y_values, '-o', label=f"Learning Rate: {learning_rate}")

    # 设置子图标题、坐标轴标签和图例
    axs[i].set_title(f"Gradient Descent (Learning Rate: {learning_rate})")
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("f(x)")
    axs[i].legend()
    axs[i].grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()