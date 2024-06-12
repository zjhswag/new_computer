import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
# print(A.dtype)

a = np.zeros((1, 5))
print(a, a.shape)
b = np.zeros(5)
print(b, b.shape)
print(a, a.shape, a+b)

a = np.array([1,1,1,1,1])
print(a, a.shape)
# a = np.arange(10)
# print(a)
#
# # access an element
# print(f"a.shape, a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")
# print(a.shape)
# # access the last element, negative indexes count from the end
# print(f"a[-1] = {a[-1]}")
#
# # index must be within the range of the vector or they will produce and error
# try:
#     c = a[10]
# except Exception as e:
#     print("The error message you'll see is:")
#     print(e)
# 赋值0
# zero_array = np.zeros((2, 3))
# print('\n', zero_array)

# 赋值1
one_array = np.ones((4, 4))
print('\n', one_array)

# 赋值0-4
# A = np.arange(4)
# A = np.random.rand(4, 4, 4)
# print('A =', A)
#
# B = np.arange(12).reshape(2, 6)
# print('B =', B)

# 矩阵乘法
# A = np.array([[3, 6, 7], [5, -3, 0]])
# B = np.array([[1, 1], [2, 1], [3, -3]])
# C = A.dot(B)
# print(C)

# 矩阵切片
A = np.array([[1, 4, 5, 12, 14],
              [-5, 8, 9, 0, 17],
              [-6, 7, 11, 19, 21]])

print(A[::], "\n")
print(A[:], "\n")
print(A[:1, ], "\n")  # 第一行
print(A[:2, :2], "\n")  # 两行两列
print(A[-2:-1, -1], "\n")  # 倒数第二行到倒数第一行，最后一列
print(A[:, :2], "\n")  # 所有行，前两列
print(A[:, 2])  # 所有行，第3列
print(A.reshape(-1, 3))