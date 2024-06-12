import numpy as np
import time


def my_dot(a, b):
    """
   Compute the dot product of two vectors

    Args:
      a (ndarray (n,)):  input vector
      b (ndarray (n,)):  input vector with same dimension as a

    Returns:
      x (scalar):
    """
    x = 0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x


np.random.seed(1)
a = np.random.rand(10000000)  # very large arrays
b = np.random.rand(10000000)
print(a, b)
tic = time.time()  # capture start time
c = np.dot(a, b)
toc = time.time()  # capture end time
print(tic)
print(f"np.dot(a, b) =  {c:.4f}")
print(f"Vectorized version duration: {1000 * (toc - tic):.5f} ms ")

tic = time.time()  # capture start time
c = my_dot(a, b)
toc = time.time()  # capture end time

print(f"my_dot(a, b) =  {c:.4f}")
print(f"loop version duration: {1000 * (toc - tic):.4f} ms ")

del a
del b
#
# np.random.seed(1)
# a = np.random.rand(1000, 100)  # very large arrays
# b = np.random.rand(100, 1000)
# print(a.dot(b))


