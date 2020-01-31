import numpy as np

arr = np.ndarray(shape =(5),dtype =int)

n = arr.size
print("Size is",n)

print('Dimension:',arr.ndim)
print('Enter %d elements'   %n)

for i in range(n):
    arr[i] = int(input("Enter element"))

print(arr)
