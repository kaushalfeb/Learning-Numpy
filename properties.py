import numpy

my_list = [10,20,30,40,50]

arr = numpy.array(my_list)

print("Array: ",arr)
print("Size: ",arr.size)
print('Datatype: ',arr.dtype)
print('Dimensions: ',arr.ndim)
print('Shape: ',arr.shape)
print('\n')

new_list = [[10,20,30],[40,50,60],[70,80,90]]
matrix = numpy.array(new_list)

print(matrix)
print('Size :',matrix.size)
print('Datatype :',matrix.dtype)
print('Dimensions :',matrix.ndim)
print('Shape :',matrix.shape)