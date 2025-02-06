from array import array

#------------------------------------------------------------------------------------#
# Taking the User Input 
#------------------------------------------------------------------------------------#
# Enter the value
arr = array('i',[])
n = int(input("Enter the length of the array"))
for i in range(n):
    x= int(input("Enter the array's next value one at a time: "))
    arr.append(x)

print(arr)

#------------------------------------------------------------------------------------#
# Search in the array
#------------------------------------------------------------------------------------#

s_val = int(input("Enter the value for search in the array: "))
k=0
for  e in arr:
    if e == s_val:
        print("Found at index number: ",k)
        break
    k+=1

#-------------------------------------unicode array-----------------------------------#
my_arr = array('u',[])
l = int(input("Enter the length for the array: "))
for i in range(l):
    x= str(input("Enter the value to insert in the array: "))
    my_arr.append(x)

print(my_arr)
# Print the array using repr() to show individual elements
print(f"array('u', {', '.join(map(repr, my_arr))})")


u_val = str(input("enter the unicode value to search in array: "))
v=0
for e in my_arr:
    if e== u_val:
        print(v)
        break
    v+=1

#---------------------------------------------------------------------------------#
# Questions: 
'''
Assignment Question:

1. Create an array with 5 values and delete the value at index number 2 without using in-built function.

2. Write a code to reverse an array without using in-built function.
'''

#------------------------
# reverse the array 
#--------------
arr1 =[2,3,4,5,6,7]
new_arr =array('i',[])
for i in arr1:
    new_arr = arr1[::-1]
print(new_arr)    

arr1 = [10,20,30,40.50]
index_to_delete = 2
for i in range(index_to_delete,len(arr1)-1):
    arr1[i]= arr[i+1]
arr.pop()
