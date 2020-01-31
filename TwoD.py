import numpy as np

m = int(input("Enter row size: "))
n= int(input("Enter coloumn size"))

matrix = np.ndarray(shape = (m,n),dtype=int)

print('Size : ',matrix.size)
print('Shape : ',matrix.shape)
print('Dimensions : ',matrix.ndim)

#Taking input from user

print("Enter %d elements of %d x %d matrix"%(m*n,m,n))

for i in range(m):
    for j in range(n):
        matrix[i,j] = int(input())

print(matrix)
