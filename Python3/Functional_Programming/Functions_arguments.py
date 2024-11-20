
#-----------------------------------------------------------------------------------------#
#                       Functional Arguments
#-----------------------------------------------------------------------------------------#

# Function Argumens
# Types of Arguments

#1.
#-----------------------------------------------------------------------------------------#
def update(x):
    print(id(x)) # print the id of the x same as a  before updating it 
    x= 8
    print(x)
    print(id(x))  # changes the id of the x 
a= 10   # here int , str are immutable so creates the different memory for a and x after updating

print(id(a))
update(a)
print("a is " , a)

#2.
#-----------------------------------------------------------------------------------------#
def update(lst):
    print(id(lst)) # print the id of the x same as a  before updating it 
    lst[1] =25
    print(id(lst))
    print("x ",lst)
lst= [10,2,30,40]   # as lst is immutable so the address in the memory is same after modifyingit
print(id(lst))
update(lst)
print('lst: ',lst)

#-----------------------------------------------------------------------------------------#
#                                        In Python
#-----------------------------------------------------------------------------------------#
'''
the a= 10 and update(a) so here the pass by value  reference or 
In python it used as  'pass by assignment' is referring to the same address for a and x 
because the x was not update and function takes the arg as  object , a =10  
'''
#-----------------------------------------------------------------------------------------#
#                                General Concept:
#-----------------------------------------------------------------------------------------#
'''
1. pass by value 
2. pass by reference
Passing the a value not the address and 
in func the x will use the diff address and a=10 will use different

2. Pass by reference:  Pass by address itself: 
means if your passing the address of the a

'''

#-----------------------------------------------------------------------------------------#
#                      Types of Arguments
#-----------------------------------------------------------------------------------------#

