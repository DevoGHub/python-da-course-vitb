import numpy as np

nparray = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

print(nparray.size)
print(nparray.shape)
nparray2 = nparray[1:2]
print(nparray2)
print(nparray)

print(nparray.flatten())