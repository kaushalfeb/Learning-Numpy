import numpy as np

my_list = [10,20,30,40]

arr = np.array(my_list)

print('Elements :')
for ele in arr:
    print(ele)

# Printing Elements using for loop

new_list = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(new_list)

print('Elements without list')

for row in matrix:
    print(row)

print('\nprinting each element of row')
for row in matrix:
    for ele in row:
        print(ele)
