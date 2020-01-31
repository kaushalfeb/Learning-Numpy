import numpy as np


new_list = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(new_list)

print(matrix)

res = matrix[:,:]
print(res)

# [row_lwr: row_upr,col_low:col_upr]

print('\n')
res = matrix[0:2,0:3]
print(res)

print()
res = matrix[1:3,1:3]
print(res)

# helps in slicing of a matrix
