
# --------------------------------------------------------------------------------------------#
#    Variable  assigning and Usages
#---------------------------------------------------------------------------------------------#

v = 2  # 2 is assign to v

print(v+3)

a= 5
print(v+a)
print(v)  # here v and a is defined so it is printing the output

# _ +20 = 22 --- We can use _ in the python interpreter for printing the previous value 

name = 'Vs code'
print(name+ ' is amazing')

print(name[3])
print(name[0:2])
print(name[3:])
print(name[3:10])
#name[0] = v  # So string in python is immutable or str does not support the item assignment 

#---------------------------------------------------------------------------------------------------#
#    Variable memory consumptions and operations
#---------------------------------------------------------------------------------------------------#

vnum =5  # it will have name value and address
print(id(vnum)) # address is - 6364378992
vname = 'jp'
print(id(vname))  # address of the variable - 703968193080

# multiple vars
a= 29
b=a # here b is refrencing to the a , so a and b is 29

print(id(a))  #140703954431288 , # here a is b is referencing to the same address and in this case py is memory efficient
print(id(b)) #140703954431288
c= 29
print(id(c)) # same add as value 29
a= 2
print(id(a))  # the address of value a will be changed , means not refrencing to 29
print(id(b)) # the address for the b is still same means b is refering to  still 29

b= 8  # Now b is refering to add of 8 , and no value is refering to 29,  so add. of 29 is reday for the garbage collection

# Garabge Collection
'''
Here the value 29 is in memory and no one using it so thats when the refrence count of and var or obejct drops to zero 
means no var is referncing to it so the memory occupied by the object is immediately dropped and it is called the 
concept of the grabage collection. 
'''
#Python uses a combination of reference counting and a cyclic garbage collector to handle this.

# Intention for the Constant Variables in py
PI = 3.14
# so PI or capitle letter should be used for the const vars.
print(type(PI))
