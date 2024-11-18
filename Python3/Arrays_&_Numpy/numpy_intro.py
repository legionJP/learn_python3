#------------------------------------------------------------------------------------#
# Numpy 
#------------------------------------------------------------------------------------#

#from array import *
# in array   2 D array doesn't support, so we need to user the numpy
#arr = array('i',[1,2,35,56], [2,3,5,6])
#------------------------------------------------------------------------------------#

# Use the Numpy for the multi Dimension Arrays
#------------------------------------------------------------------------------------#
from numpy import *
arr = array([1,2,35,56])
arr1 = array([1,2,35,56],int) # can use the type to mention in the end
print(arr)

#------------------------------------------------------------------------------------#
 #  Ways for creating Array using the Numpy
#------------------------------------------------------------------------------------#

'''
There is 6 ways for creating the arrays 
1. array() ,2. linspace() 3. logspace() , 4. arange() , 5. zeros(), ones()

'''

#------------------------------------------------------------------------------------#
#   1. array()
#------------------------------------------------------------------------------------#

arr = array([1,2,3,4,5])
print(arr.dtype)

arr2 = array([1,2,3,4,5.0]) # all the values will be converted into the float implicitly bcz all th value should be same type 
arr2 = array([1,3,4,5,6],float)

print(arr.dtype)

#------------------------------------------------------------------------------------#
#   2. linspace()
#------------------------------------------------------------------------------------#

arr = linspace(0,16,10)
# Here 15 is included in the range,and the 10 is the parts to divide the 
# range into parts
print(arr)
arr1 = linspace(0,15,16)
print(arr1)

arr2 = linspace(0,15) # 15 parts by default 
print()
print(arr2)

#--------------------------------------------------------------------------------------#
#  3. arange()
#--------------------------------------------------------------------------------------#
arr = arange(1,15,2) # start , stop , step
print(arr)


#--------------------------------------------------------------------------------------#
#  3. logspace()
#--------------------------------------------------------------------------------------#
arr = logspace(1,40,5) 
# the number 5 is for 10 raise to 1 to 10 raise to 40 and will be divided into 5 parts
print(arr)