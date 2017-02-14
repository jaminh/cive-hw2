import numpy as np

x = np.random.rand(2,2)
print(x)
print(type(x))
print(x.size)
print(x.shape)
print(x.dtype)

y = np.transpose(x)
print(y)

print("Addition")
print(x + y)

print("Multiplication")
print(x * y)
