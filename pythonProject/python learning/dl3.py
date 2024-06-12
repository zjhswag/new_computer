import numpy as np
import math
import time
#比较loop和dot运算
def my_dot(a, b): 
    x=0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x
# test 1-D
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
print(f"my_dot(a, b) = {my_dot(a, b)}")
print(a.shape)

b=b*a
print("**",b)
# test 1-D
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
c = np.dot(a, b)
print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape} ") 
c = np.dot(b, a)
print(f"NumPy 1-D np.dot(b, a) = {c}, np.dot(a, b).shape = {c.shape} ")

np.random.seed(1)
a = np.random.rand(10000000)  # very large arrays
np.random.seed(1)
b = np.random.rand(10000000)
print(a)
print(b)

tic = time.time()  # capture start time
c = np.dot(a, b)
toc = time.time()  # capture end time

print(f"np.dot(a, b) c is=  {c:.4f}")
print(f"Vectorized version duration: {1000*(toc-tic):.4f} ms ")

tic = time.time()  # capture start time
c = my_dot(a,b)
toc = time.time()  # capture end time

print(f"my_dot(a, b) =  {c:.4f}")
print(f"loop version duration: {1000*(toc-tic):.4f} ms ")
x=0
tic = time.time()
c=b*a

for i in range(c.shape[0]):
     x+=c[i]
 
toc = time.time()
print(f"loop2 version duration: {1000*(toc-tic):.4f} ms ")

del(a);del(b); del(c) #remove these big arrays from memory

