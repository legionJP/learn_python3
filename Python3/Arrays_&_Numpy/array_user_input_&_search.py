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

# Search in the array

s_val = int(input("Enter the value for search in the array: "))
k=0
for  e in arr:
    if e == s_val:
        print("Found at index number: ",k)
        break
    k+=1

my_arr = array('u',[])
l = int(input("Enter the length for the array: "))
for i in range(l):
    x= str(input("Enter the value to insert in the array: "))
    my_arr.append(x)

print(my_arr)

u_val = str(input("enter the unicode value to search in array: "))
v=0
for e in my_arr:
    if e== u_val:
        print(v)
        break
    v+=1

