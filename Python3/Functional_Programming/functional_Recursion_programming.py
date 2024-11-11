''''
# Recursion is used for the 
1 . Repetative Problems 
2. complex  Structures 

# When Implemanting the recursion always consider ethe result , if don't it will spin into infinte loop and 
#crash the system

#Recursion

def new_func(obj):
    #some logic Like base case and condtion 
    return new_func(obj)

 '''

 # Looping solution by recursion

def find_factorial_looping(n):
    if n<0:
        return 0
    else:
        factorial =1
        for i in range(1,n+1):
            factorial=factorial*i
        return factorial
print(find_factorial_looping(5))       

#recursive solution
def find_factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*find_factorial_recursive(n-1) # here retrun is keeping the refference of implemented value and calling again and again 
print(find_factorial_recursive(5))  

'''#Advantages of  the Recursion 
1. Neet code 
2. Sub- Problems 
3. Easy Sequences 
Disadvantages:

Hard to follow the logic 
Memory , some time efficeint and some time high consuming 
Debugging : hard to debug 



'''
#recursive function for the tower of hanoi:

disks=int(input('Number of disks to be placed: '))
source=str(input('Name of the source tower '))
helper=str(input('Name of the  Helper '))
destination= str(input('Name of the destination '))    

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
 