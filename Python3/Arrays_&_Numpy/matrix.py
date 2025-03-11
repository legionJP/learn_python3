#------------------------------------------------------------------------------------#
#              Working with Matrix and  Numpy 
#------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------#
# Working with the arrays in Numpy
#------------------------------------------------------------------------------------#
from numpy import * 
# 2 array inside one big array 
arr1 = array([
    [1,2,3,4,9,11],[5,6,7,8,12,13]
])

print(arr1)

print(arr1.dtype)
print(arr1.ndim) # give the type of the dimension
print(arr1.shape) # Number of rows and column
print(arr1.size)

arr2 =arr1.flatten() # convert the multidimensional to single dimensional 
print(arr2)

arr3 = arr2.reshape(3,4) # will create the 2 D array from 1 D array
print(arr3, arr3.ndim)
print("\n")

arr4 = arr2.reshape(2,2,3) 
# It will have two 2D array and each 2 D array  will have  two 1-D array with 3 values
print(arr4, arr4.ndim)

#------------------------------------------------------------------------------------#
#                 Creating the Matrix
#------------------------------------------------------------------------------------#

# 1. Converting  array into the Matrix 
arr= array([[1,2,3,4],
            [5,6,7,8]
])

m = matrix(arr)
print(m)
print('------------------------')
#------------------------------------------------------------------------------------#
# 2.create the matrix by manually or input  :

m= matrix('5 6 7; 8 4 5; 6 3 7')  # it will be of 3 rows and 3 column 
print(m)

# printing the diagonal 
print(diagonal(m))
print(m.min())
#------------------------------------------------------------------------------------#
# 3. Multiplying the Matrices

m1= matrix('5 6 7; 8 4 5; 6 3 7')  
m2= matrix('2 3 5; 1 5 7; 7 9 8')
m3= m1* m2
print(m3)
#------------------------------------------------------------------------------------#