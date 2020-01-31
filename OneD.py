import numpy as np

n = int(input("Enter size"))

arr = np.ndarray(shape =(n),dtype = int)

print('Enter %d elements'%n)

for i in range(n):
    arr[i] = int(input("Element "))

print(arr)
