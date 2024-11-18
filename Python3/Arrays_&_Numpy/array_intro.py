#-----------------------------------------------------------------------------------------#
#                                Array
#-----------------------------------------------------------------------------------------#
#-->
# similar to list but need to have the value of the same type , Like int array , str array 
# Type of Array:
'''
1. Single Dimension Array 
2. Multi Dimesion Array
'''

#Use of Array: --- 
'''
10 students in class than need to create the  10 different vars. for the marks like m1, m2,
for each students marks ,but we can create the array to fix it 
'''
#------------------------------------------------------------------------------------#
# Importing the modules with different types
'''
import array # use array.array
import array as arr   # can use arr.array
from array import * # only use array 
from array import array # use array keyword only and import only array module
'''
from array import array
#------------------------------------------------------------------------------------#
arr = array('i',[1,7,9,4,5,-5]) # for the type code go to the array.md # here arr is int object
arr1 = array('I',[1,2,3,4,5]) # only unsigned int no negative value
print(arr)
print(arr[0])

# Info about the array
print(arr.buffer_info()) # (126459862695504, 6)--tuple--> address , size
print(arr.typecode)
#------------------------------------------------------------------------------------#
# Working with the Int type array
#------------------------------------------------------------------------------------#

# Add, append and reverse the array
arr.reverse()
print(arr)
arr.reverse()

# 
for i in range(len(arr)):
    print(arr[i])

for e in arr:
    print(e)
#------------------------------------------------------------------------------------#
# Working with the char type array
#------------------------------------------------------------------------------------#
vals = array('u',['a','b','c','d'])
for i in vals:
    print(i)
#------------------------------------------------------------------------------------#
# Creating the new array  with the same value
#------------------------------------------------------------------------------------#

new_arr= array(arr1.typecode,(a for a in arr1)) # take the typecode form arr1 and assign the each value in arr
print(new_arr)

sqr_arr = array(arr1.typecode,( a*a for a in arr1))
print(sqr_arr)  # here 1st a is var. acting as a placeholder and takes the each vale of the arr1

# using while in array
i= 0
while i<len(sqr_arr):
    print(sqr_arr[i])
    i+=1
#------------------------------------------------------------------------------------#

#-------------------------------------------------- problem on swap #--------------------------
from typing import List
def swapN(a:list, b:list) -> None:
    a[0],b[0] =b[0],a[0]
    print(a[0],b[0])

a,b= map(int,input().split())
a_1,b_1= [a],[b]
swapN(a_1,b_1)
