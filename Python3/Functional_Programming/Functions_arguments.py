
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
#                     2. Types of Arguments:
# 1. Formal Arguments  2. Actual Arguments
#-----------------------------------------------------------------------------------------#

def add(a,b):    # a, b is the formal arguments
    c = a+b
    print(c)

add(3,2)    # here 3, 2 is the actual arguments 


#-----------------------------------------------------------------------------------------#
#                  Actual Arguments 
#-----------------------------------------------------------------------------------------#
#1. Postion #2. Keyword  # 3. Default  #4. Variable length  argumetns
 
def person(name, age=18):
    print(name,age)
person('JP',23)     # This is using the postions to assign the value to param
person(name='I', age='Dont Know') # this is Using the keyword element argument , bcz name and age are keyword and we can use it when don't know about the sequence of args
person('You') # Default: here if the age is not passed then we can give the default age and it will be used when no age value is passed
#-----------------------------------------------------------------------------------------#

#1. Variable length argument : (*arg)
#-----------------------------------------------------------------------------------------#
#  Means you can define a function where number of arguments are not fixed

#def sum(a,*b): we can only use the *b  as arg and sum it but need to put c=0 instead of c=a
def sum(a,*b):   # here the *b is tuple and it can store the multiple value and iterate from over it and store the values
    c=a
    for i in b:
        c+=i
    print(c)    
sum(23, 5,3,5,6)    

#2. Keyworded Variable length Argument (**kwarg)
#-----------------------------------------------------------------------------------------#
# In this when you pass the parameters you have also need to mention the keywords

def persons(name, **data):
    print(name, data)
    for i , j in data.items(): # to print he key, value from data 
        print(i,j)
persons('You', age=21, city = 'Hometown',mob=916000016)


#-----------------------------------------------------------------------------------------#