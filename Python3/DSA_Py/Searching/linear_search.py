#--------------------------------------------------------------------------------------------------------------#
#                                         Linear Search 
#--------------------------------------------------------------------------------------------------------------#

position =-1

# Using the While loop
def search(list,n):
    i =0
    while i<len(list):
        if list[i]==n:
            globals()['position'] =i
            return True
        i =i+1
    return False


arr = [5,8,4,6,9,2]
# Search for 9 
n=2

if search(arr,n):
    print("found at ",position)
else:
    print("Not found")    
#--------------------------------------------------------------------------------------------------------------#
#                                   Using the For loop
#--------------------------------------------------------------------------------------------------------------#

pos=-1
current_index=0

def for_search(lst,n):
    global current_index
    for i in lst:
        if i == n:
            globals()['pos']= current_index
            return True
        current_index +=1

    return False

if for_search(arr,5):
    print("Found at ",pos)
else:
    print("Not Found")    
#--------------------------------------------------------------------------------------------------------------#
#                                   Using the enumerate()
#--------------------------------------------------------------------------------------------------------------#

def for_search1(lst,n):
    global i
    for i, j in enumerate(lst):
        if j == n:
            return i, True
    return False

# Below is using the unpacking for index and found as found return the true and 
# index will be i so no need to use i as gloal var

index , found = for_search1(arr,9)
if found:
    print("Found at ",index)
else:
    print("NOT  Found ")    

# Using the  i as global variable
if for_search1(arr,9):
    print("Found at ",i)
else:
    print("Not found")

#--------------------------------------------------------------------------------------------------------------#