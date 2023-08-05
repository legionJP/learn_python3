'''Function take inputs and gives output 

2 Types of functions: 
1. Traditional

-> Function programming utilies the function for the clean ,consitent and maintainable code 

-> functional programming is differntiate by design comapare to object oriented.
-> does not change the data outside the scope of the function , its only returned the function result
that is being called .

. the function is being considered as a standalone and independet .

-> Many object oriented programming langauges has aided  the functional programming.
-> In python functions are called first class citizen ,Means they have same level of functions , strings and Numbers 

-> fun.can be assign to varriable   passed as an argument  and returned can returned as its caller.

-> In function programming the logic  for certain tasks is already built in and function can 
be resuable , and save a lot of development time. 


Note: :: slice function that is used to include wthe list item after the index value or before the index Value
like ::-1 and :: 1

'''

'''
2. Pure functions : 
It is the function that does not have the data list or function and can't afftect beyond 
it's scope .

def add_list(lst,item):
n1 = lst.copy()
n1.append(item)
return n1

* Know the outcome
* Consistent and reliable
* cache 
* Multi threaded program
* pure function prevents changes on global scopes 

'''

# Altering the Pure Functions

my_list = [1,2,3,4]
def  add_list(item):
    return my_list.append(item)

add_list(4)

print(my_list) # data is manipulated at the global stage


#alternig the function 

my_list = [1,2,3,4]
def  add_list(item):
    my_list.append(item)
    return my_list 
new_list=add_list(5)

add_list(4)
print(my_list)
print(new_list)

#:Pure Function

my_list1 = [1,2,3,4,5]

def add_list(lst,item):
    new_list= lst.copy # new list creating the copy 
    new_list.append(item)
    return new_list

new_list =add_list(my_list1,6)
print(new_list) # original list 
print(my_list1) #here pure fucntion doesn't change the original list at global scope



