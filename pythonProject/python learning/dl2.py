import numpy as np    # it is an unofficial standard to use np for numpy
import time

a = np.zeros(4);                
print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,4));             
print(f"np.zeros(4,4) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = 6*np.random.random_sample((4,3))+0; #b-a*np.random.random_sample+a(在b和a中生成随机数)
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4);                
print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,));             
print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4); 
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

#vector slicing operations
a = np.arange(10)
b=np.arange(2,10,2);
print("b is",b)
print(f"a         = {a}")

#access 5 consecutive elements (start:stop:step) 
c = a[2:7:1];     print("a[2:7:1] = ", c)

# access 3 elements separated by two 
c = a[2:7:2];     print("a[2:7:2] = ", c)

# access all elements index 3 and above
c = a[3:];        print("a[3:]    = ", c)

# access all elements below index 3
c = a[:3];        print("a[:3]    = ", c)

# access all elements
c = a[:];         print("a[:]     = ", c)

a = np.array([1, 2, 3, 4])

# multiply a by a scalar
b = 5 * a 
print(f"b = 5 * a : {b}")