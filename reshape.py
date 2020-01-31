import numpy as np

my_list = [10,20,30,40,50,60]

arr = np.array(my_list)

print("Array:",arr)
print('Dimension:',arr.ndim)

res = arr.reshape(2,3)
print(res)
print("Dimension",res.ndim)

new_list = [10,20,30,40,50,60,70,80]

newarr=np.array(new_list)

holder = newarr.reshape(2,2,2)

print(holder)
