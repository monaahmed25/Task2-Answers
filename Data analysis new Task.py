
import numpy as np
array_A=np.array([10,20,30,40,50])
array_B=np.array([5,4,3,2,1])
print(array_A+array_B)
print(array_A-array_B)
print(array_A*array_B)
print(array_A/array_B)
print(array_A.ndim)
y=array_A.sum()
x=array_A.size
mean=y/x
print(mean)
print(array_A.min())
print(array_A.max())
reshape_array=array_A.reshape(5,1)
print(reshape_array)
array_z=array_A*array_B
print(array_z.sum())

