# Already Describes in detailed in the Functional Programming

#-------------------------------------
#If you want 'n' for each 'n' in nums 
#-----------------------------------

Nums= [1,2,3,4,5,6,7,8,9,10,11,12]
Num_list =[]
for n in Nums:
    Num_list.append(n)
print(Num_list)

# By using the list comprehension
Num_list = [n for n in Nums]
print(Num_list)

#--------------------------------
# Using the Lambda + Map function
#--------------------------------

'''
map(): The map() function applies a given function to each item of an iterable 
(such as a list or tuple) and returns a list of the results. 
 example, you can use map() to square all numbers in a list.
'''
Nums= [1,2,3,4,5,6,7,8,9,10,11,12]
Num_list1 =map(lambda n: n*n, Nums)
print(Num_list1)
Num_list1=list(Num_list1)
print("the num list is",Num_list1)


# for 'n' for each n in nums if n is even

Num_list=[]
for n in Nums:
    if n%2 ==0:
        Num_list.append(n)
print(Num_list)


#--------------------------------
# By  Using the Lambda + filter function
#--------------------------------

'''
 The filter() function constructs a list from elements of an iterable for which a function returns true.
In simple words,it filters the given iterable with the help of a function that 
tests each element in the iterable to be true or not.
'''

Num= [1,2,3,4,5,6,7,8,10]
Num_list1=filter(lambda n: n%2 == 0, Num) 
#print(Num_list1)      #printing the location o f filter object !
Num_list1 = print(list(Num_list1))

#------------------------------
#By using the list COmprehension
#-----------------------------

Num_list1=[n for n in Num if n%2 ==0]
print(Num_list1)

#=========================================================================================
# if  we want a (letter, num ) pair fo each letter in 'abcd ' and each number in '0123'
#---------------------------------------------------------------------------

Num_list =[]
for letter in 'abcd':
    for num in range(4):Num_list.append((letter,num))
print(Num_list)    

#By  using the list comprehension

Num_list =[(letter,num) for letter in 'abcd' for num in range(4)]
print(Num_list)

#===================================
# Dictionary comprehension 
#----------------------------------

names =['JP', 'AK', 'MM', 'DP', 'Wade']
Department=['IT', 'food', 'Trade','Security', 'paav']
#print(zip(names,Department))
my_dict = {}
for names , Department in zip(names, Department):
    my_dict[names]=Department #here names is the key and Department is value
print(my_dict)

#Dictionary comprehension , name and dept are iterables

my_dict1={name: Dept for name, Dept in zip(names,Department)}   
print(my_dict1)

#=====================
#Set Comprehensions
#------------------

nums ={1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9}
print(type(nums))
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)

#type 2 
my_set ={n for n in nums}
print(my_set)

#-----------------------
#Generator Expression
#-------------------

#  I want to yield n*n for each 'n' in nums
nums=[1,2,3,4,5,6,7,8,9,10]

def gen_fun(nums):
    for n in nums:
        yield n*n

my_gen =gen_fun(nums)
print("values",list(my_gen))  
 
#my_gen =(n*n for n in nums)
for i in my_gen:
    print(i)   


#example of list comprehensions

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# elements=[(x, y , z) for i in range(0,x+1) for j  in range(0, y+1) for k in range(0,z+1) if i+j+k!=n]
# print(elements)``