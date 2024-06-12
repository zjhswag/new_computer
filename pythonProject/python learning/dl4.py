import numpy as np
import math
import time
# show common Course 1 example
X = np.array([[1,2],[2,2],[3,4],[4,5]])
a=np.array([1,2,3,4,5])#数组
print(a)
#a = np.zeros((3,8))
d=np.array([[1,2,3],[2,2,3]])#矩阵2行3列
print(d)
print(d.shape)

print(X)
print(X.shape)
w = np.array([[2],[3]])
print(w)
c = np.dot(X[1], w)
print(c)#c是一个数字
print(f"X[1] has shape {X[1].shape}")
print(f"w has shape {w.shape}")
print(f"c has shape {c.shape}")


#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)#reshape将矩阵改成2行10列
print(f"a = \n{a}")

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
