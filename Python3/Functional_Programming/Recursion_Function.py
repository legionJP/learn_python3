
#----------------------------------------------------------------------------------------#
#                                      Recursion
#----------------------------------------------------------------------------------------#
import sys
''''
# Recursion is used for the 
1. Repetative Problems 
2. Complex  Structures 

> When implemanting the recursion always consider either result,
if don't it will spin into infinte loop and crash the system
'''
#Recursion
#The goal in the recursion of function to find the base case condtion if it finds it terminated
#----------------------------------------------------------------------------------------#
sys.setrecursionlimit(2000) # set the default limit to 2000 from 1000
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    if i>=1998:    # Base case to not get the warring for the limit    
        print("limit is reached for the recursion at ",i) 
    else:  
      i+=1
      print("hello",i)
      greet()    # Calling the function itself and max range is 1000 to cppe with recursion    
greet()

#2
def new_func(obj):
    #some logic Like base case and condtion 
    return new_func(obj)


#----------------------------------------------------------------------------------------#
#                 Looping solution by recursion
#----------------------------------------------------------------------------------------#

def find_factorial_looping(n):
    if n<0:
        return 0
    else:
        factorial =1
        for i in range(1,n+1):
            factorial=factorial*i
        return factorial
print(find_factorial_looping(5))       

#----------------------------------------------------------------------------------------#
#                          Recursive solution
#----------------------------------------------------------------------------------------#
def find_factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*find_factorial_recursive(n-1) # here retrun is keeping the refference of implemented value and calling again and again 
print(find_factorial_recursive(5))  


#----------------------------------------------------------------------------------------#
#                       Advantages and Disadvantages of  the Recursion: 
#----------------------------------------------------------------------------------------#
'''
# Advantages of  the Recursion: 
1. Neet code 
2. Sub- Problems 
3. Easy Sequences 

# 2. Disadvantages:

Hard to follow the logic 
Memory , some time efficeint and some time high consuming 
Debugging : hard to debug 

'''
#----------------------------------------------------------------------------------------#
#          Recursive function for the tower of hanoi:
#----------------------------------------------------------------------------------------#

disks=int(input('Number of disks to be placed: '))
source=str(input('Name of the source tower '))
helper=str(input('Name of the  Helper '))
destination= str(input('Name of the destination tower '))    

def hanoi(disks,source,helper, destination):
    
    #Base condition
    if (disks ==1):
        print('disk {} moves from tower {} to tower {}' .format(disks,source,destination))
        return 0
    else:

    #recursive call when function will call itself
        hanoi(disks-1,source,destination,helper)
        print("disk {} moves from tower {} to tower {}" .format(disks,source,destination))
        hanoi(disks-1, helper, source,destination)
        return hanoi
hanoi(disks,source,helper,destination)