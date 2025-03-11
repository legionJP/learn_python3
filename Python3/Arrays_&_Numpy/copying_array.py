from numpy import * 

arr = array([1,2,3,4,5])
arr1 = array([6,7,8,9,10])
arr3 = arr+5
arr4 = arr+arr1 # vECTORIZED OPERATIONS
print(arr3)
print(arr4)

print(sin(arr))
print(log(arr), sqrt(arr))
print(min(arr1),max(arr1))
print(concatenate([arr,arr1]))
#------------------------------------------------------------------------------------#
# Copying the arrays
arr5 = arr1
print(arr1)
print(arr5)
print(id(arr5),id(arr1)) 
# It is called the alising bcz both array are pointing to the same address

#------------------------------------------------------------------------------------#
# Copying the array with the different addres
#------------------------------------------------------------------------------------#
'''
 Types of Cpoying in the Python : 
 1. Shallow Copy : Copy the element but both the array are still dependent on each other 
 2.  Deep Copy :
''' 
arr6 = arr.view() # create the array at the different address ,  but elements points to the same object in memory 
arr[1]= 7  # changes both array due to shallow copy

print(arr6,arr, id(arr6), id(arr))
#------------------------------------------------------------------------------------#
# Deep Copy
#------------------------------------------------------------------------------------#
arr6 = arr.copy() # create the array at the different address
arr[1]= 8  # changes only the arr array due to Deep copy

print(arr6,arr, id(arr6), id(arr))
#------------------------------------------------------------------------------------#

