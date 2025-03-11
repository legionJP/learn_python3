#--------------------------------------------------------------------------------------------------------------#
#                                         Binary Search 
#--------------------------------------------------------------------------------------------------------------#
# If the list lenght is very long then the search will be very long and mem consuming

# All the value have to be sorted
# Search value = 45
# Specify THE LOWER BOUND  And Upper bound
# mid index = (lower+Upper)/2 = (0+5)/2 = 2 (int div)
# mid = 2--->8
# Now check , mid == search Value or not , if == return true
# if Search Value is smaller than the mid value so change the upper bound to mid value+1 ----> Mid becomes Upper 
# and if the search value is bigger than the mid value then change the lower bound to mid value-1----> Mid becomes Lower

# Repeat alll the process when the value is not found 


pos =-1

def search(list ,n):
    l =0
    u = len(list)-1

    while l<=u:
        mid = (l+u)//2
        if list[mid] ==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                l =mid+1
            else: 
                u =mid-1

    return False
list = [2,3,4,6,7,8,9,10,6789,9945]
n =911
if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not found")    



#--------------------------------------------------------------------------------------------------#

position =-1
def bi_search(lst,n):
    l=0
    u = len(lst)-1
    while l<=u:
        mid = (l+u)//2
        if lst[mid]==n:
            globals()['position']= mid
            return True
        else:
            if list[mid] < n:
                l = mid+1

            else:
                u = mid-1
    return False

lst = [1,2,3,4,5,6,9,88,888,999]
n= 888
if bi_search(lst,n):
    print("found at ", position+1)
else:
    print("Not found")                

# 1,2,3,4,5,6,7===l=1,u=7 --. n=5, l=0 , u=6 , mid = 3 , 4!=n , 4<5, l =3+1 , u =6  == mid=4 , , true
