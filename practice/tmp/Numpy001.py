import numpy as np

a_list = list(range(10))
b = np.array(a_list)
print(type(b))

a = np.zeros(10, dtype=int)
print(type(a))
print(a.dtype)


a = np.zeros((4,4), dtype=int)
print(a.dtype)
print(type(a))
print(a)

a = np.ones((4,4), dtype=float)
print(a.dtype)
print(type(a))
print(a)

a = np.full((4,4), 3.14)
print(a.dtype)
print(type(a))
print(a)
