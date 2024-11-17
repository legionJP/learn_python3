#-----------------------------------------------------------------------------------------#
#                                Array
#-----------------------------------------------------------------------------------------#
#-->
# similar to list but need to have the value of the same type , Like int arrya , str array 
#Use of Array: --- 
'''
10 students in class than need to create the  10 different vars. for the marks like m1, m2,
for each students marks ,but we can create the array to fix it 
'''

import array # use array.array
import array as arr   # can use arr.array
from array import * # only use array 

arr.array




#-------------------------------------------------- problem on swap #--------------------------
from typing import List
def swapN(a:list, b:list) -> None:
    a[0],b[0] =b[0],a[0]
    print(a[0],b[0])

a,b= map(int,input().split())
a_1,b_1= [a],[b]
swapN(a_1,b_1) 