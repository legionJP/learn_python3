#----------------------------------------------------------------------#
#                            FUNCTIONS
##----------------------------------------------------------------------#

'''Function take inputs and gives output 

2 Types of functions: 
1. Traditional 2. Pure Functions
'''
#----------------------------------------------------------------------------------------#
#                            1. Traditional Functions
#----------------------------------------------------------------------------------------#
'''
-> Function programming utilies the function for the clean ,consitent and maintainable code 

-> functional programming is differntiate by design comapare to object oriented.
-> does not change the data outside the scope of the function ,
 its only returned the function result
that is being called .

> the function is being considered as a standalone and independet .

-> Many object oriented programming langauges has aided  the functional programming.
-> In python functions are called first class citizen ,
Means they have same level of functions , strings and Numbers 

-> fun.can be assign to varriable  passed as an argument 
 and returned can returned as its caller.

-> In function programming the logic  for certain tasks is already built in and function can 
be resuable , and save a lot of development time. 

Example: :: slice function that is used to include the list item after the index value or before the index Value
like ::-1 and :: 1

'''
#----------------------------------------------------------------------------------------#
#                                 2. Pure functions : 
#----------------------------------------------------------------------------------------#
'''
It is the function that does not have the data list or function and can't afftect beyond 
it's scope .

* Know the outcome
* Consistent and reliable
* cache 
* Multi threaded program
* pure function prevents changes on global scopes 

'''
def add_list(lst,item):
    n1 = lst.copy()
    n1.append(item)
    return n1
list = add_list([1,2,3,4],6)
print(list)

#----------------------------------------------------------------------------------------#
#                   Altering the Pure Functions
#----------------------------------------------------------------------------------------#

my_list = [1,2,3,4]
def  add_list(item):
    return my_list.append(item)
add_list(5)
print(my_list) # data is manipulated at the global stage

#----------------------------------------------------------------------------------------#
#2.
my_list = [1,2,3,4]
def  add_list(item):
    my_list.append(item)
    return my_list 
new_list=add_list(5)

add_list(4)
print(my_list)
print(new_list)

#----------------------------------------------------------------------------------------#
#                                alternig the function 
#----------------------------------------------------------------------------------------#
#:Pure Function

my_list1 = [1,2,3,4,5]

def add_list(lst1,item1):
# append the item in the new list
    #new_list= my_list.copy()
    new_list = lst1.copy()
    print("This is new list ",new_list) # original list 
    new_list.append(item1)
    return new_list

append_list= add_list([1,2,3,4],6)
print("this is appended list", append_list)
print(my_list1) #here pure fucntion doesn't change the original list at global scope

#----------------------------------------------------------------------------------------#
#         Calling the function By differnt ways
#----------------------------------------------------------------------------------------#
def add_sub(a,b):     # takes arguments or param
    c =a+b
    d = a-b
    print(c)
    print(d)
    return c,d 
add_sub(5,4)
r1,r2 = add_sub(9,2)
result = add_sub(6,4)  # when using the object the function Expecting someting to return

#-----------------------------------------------------------------------------------------#