'''There are four main types of comprehensions in Python: 

List comprehension 

Dictionary comprehension 

Set comprehension 

Generator comprehension'''

# List Compression: 

# 1. Updating the same list 

data =[1,2,3,4,5,6,22,44,54]

new_data=[x+4 for x in data]
print("updating the list",data)

#2. Updating the list : with new list 

update_list=[x*x for x in new_data]
print("update the list ",update_list)

#3. Updating the list with if condition

new_list=[x for x in update_list if x%2==0 ]
print("list divisile by two",new_list)

# Alternate apporach 

list1= [x-1 for x in new_list if x%2 ==0]
print("thi is divsible by number -1 ",list1)

# using the range funvtion

range_data=[x for x in range(100) if x%2 ==0]
print( "divisible by 2 in range of 99 ",range_data)


for x in range (len(data)):
    data[x]= data[x]+3
print(data)    

# Dictionary Comprehension

#Syntax 
 #dict = { key:value for key, value in <sequence> if <condition> } 

# Using range() function and no input list

using_range={x:x*2 for x in range(28)}
print('using range the dict is ',using_range)


# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

#using the one input to create the list 

input_list={x:x**2 for x in number }
print('dict using the one input of list',input_list)


#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.


#using the two input of the list 

month_dict ={key:value for (key,value) in zip(number ,months)}
print(month_dict)


#Set comprehnsion

#The set comprehension deals with the set data type and it's very similar to list comprehension. 
#The only key difference is the use of curly brackets for sets instead of square brackets as in lists. For example:

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

set_b ={x for x in range (12,30) if x not in [12,23,24,27]}
print(set_b)


#Generator Comprehension

#enerator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
#  They are also more memory efficient as compared to list comprehensions.

data=[ 2,3,5,7,9,11,13,15,17,19,21]
gen_object=(x for x in data)   # use the curve brackets for the iterating the generator 
print(gen_object)
print(type(gen_object))

for items in gen_object:      #he elements in this iterator object cannot be directly accessed and need the help of a for loop and as such, I iterate over these elements and print them.
    print(items, end= " ")

 

def square(num):
    return num * 2

new_data1=map(square,data)
#new_data1=[x+3 for x in data]
print(new_data1)
for items in new_data1:
    print(items)
    print(items,end= " ")


#concating the two list item 
a =[[96],[69]]
print("".join(list(map(str,a))))   


#lambda function
# lambda arguments: expression

num = [1, 2, 3, 4] #input list, 2nd argument 
added_two = map(lambda i: i + 2, num)      #output list object 
print(list(added_two))   

# Using lambda with map() to double each element of a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# Using lambda with filter() to keep even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]
