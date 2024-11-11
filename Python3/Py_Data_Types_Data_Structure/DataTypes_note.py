#_____________________________________________________________________________________________________________
#                                          Intro to Data_Types in python: -
#______________________________________________________________________________________________________________

# ---> Builtin Data Types : Booleans, Numbers, String, Sequences and Collections , Built-in Constants
# ---> Special data type: None or NoneType , bool, bytes, bytearray, memoryview, frozenset, complex, Ellipsis,type

#none is special data types that represents the absence of a value or a null value.

#1.) Booleans Data Types: - bool (True, False)

#2.) Numereic data types - Integer (int), Float, Complex Number , bool (it is subclass of the integer type (int) and used in numerical operations wher 1 is true and 0 is false)

#3.) Sequence Data Types - String, List, Tuples , (Range)

#4.) Collection Data Types: List, Tuple , Set , String, Dictionary


#1.) Booleans Data Types: -
#--------------------------
#  bool: A boolean value of either True or False. Logical operations like and, or, not can be performed on booleans.
print(int(True)) # 1
print(int(False)) # 0
"""
The bool type is a subclass of the int type and  True and False are its only instances:

issubclass(bool, int) # True
isinstance(True, bool) # True
isinstance(False, bool) # True
If boolean values are used in arithmetic operations, 
their integer values (1 and 0 for True and False) will be used to
return an integer result:
True + False == 1 # 1 + 0 == 1
True * True  == 1 # 1 * 1 == 1
"""
#-------------------------------------------------------------------------------------------------
#2.) Numereic data types - Integer, Float, Complex Number 
#-------------------------------------------------------------------------------------------------#

num = 2.6
print(type(num)) # ---> <class 'float' >
num= 6
print(type(num)) # int
num = 6+9j
print(type(num)) # complex numb

a = 12.12
b = int(a) # the type will be coverted to the int 
f= float(b)

# normal to complex 
f =6
c = complex(b,f)
print(c)
print(type(c))

print(b>f)
bl = b>f
print(type(bl)) 

#--------------------------------------------------------------------------------------------------------#
#3.) Sequence Data Types - String, List, Tuples , (Range)

#4.) Collection Data Types: List, Tuple , Set , String, Dictionary

'''
all sequences are collections, but not all collections are sequences. 
The main distinction is that sequences are ordered and support indexing,
whereas collections have a broader definition, including unordered types like sets and dictionaries.
''' # See the diffrence in last between the sequence and collection

#===============================================================================================#

#----------------
# String : - 
#---------------
#String is a sequence of characters that is enclosed in signle or double quotes.

# str: a unicode string. The type of 'hello'
# bytes: a byte string. The type of b'hello'  

#reversed: A reversed order of str with reversed function:
a = reversed('hello')
print(a)

#=================================================================================================#

#--------
# List:-
#--------
# List are essentially an array and hold any type data inside square bracktes :

list1=[1,'hello',4.5, "A"] 
list2=[1,2,3,4,5]
list3=[1,[1,2,3,],4,5,6]

'''
for x in list1:
    print('value',x) #in a list x will run for the number of times of list's number. 
print(list1)
#2
x = enumerate(list1)
for index , value in x:
   print("Index {index}: {value}")
'''

#enumerate() fun.
x=enumerate(list3)
print('enumeration', list(x))

print(list3)
print(list1, sep=" ")

list1.insert(len(list1), 6)# 1st method of inseritng item str a specified index

list1.append(6)  #second method of the inserting the number so The append function appends a single item without having to specify the index.

list1.extend([7,8,9,10]) # another function for addding the multiples itemm
#________________________________
#Deleting the item from the lsit :

#list.pop(1)
#del list(5)

#==========================================================================================#

#-------------------
#  Tuples: 
#-------------------
#An ordered collection of n values of any type ( where n >= 0, means tuple can hold 0 or more than 0 values )

#1.) values inside the tuple can't be modified or changed : 
tuple1=(1,'hello',8.9,"A")

#2.) we can declare tuple without using the paranthesess
my_tuple1 = 1,'tuple',6.45,'name',True

#3.)Tuple exmples :

my_tuple=(1,'tuple',6.45,'name',True)

print(my_tuple)
print(my_tuple[1])
print(type(my_tuple))

print(my_tuple.count('tuple'))
#print(my_tuple.index('6.45'))
# for x in my_tuple:
#     print(x)
#print(my_tuple.index('6.45'))

for x in my_tuple:
    print(x)

#assigninng the vale to the tuple:

# my_tuple[0]=5  
# It will not assign the value because anything that is in the tuple is immuteable

#====================================================================================================#

#---------------
#Dictionary :-
#--------------
#Dictionary store data in key value structure : and key should be uinque
dict={'a':22, 'b':44.4}
print('a')
name= {'jp': 'myname', 'you': 'yourname', 1: 23}
print(name)
print(name.keys())
print(name.values())
print(name['jp'])
print(name.get('you'))
                                                          
#Boolean: type(true), type(false)

#-----------------------------------------------------------------------------------------------------#
# set : -
#---------------------------------------------------------------------------------------------------#
example_set={1,'hello',4.5,"A"}


#-----------------------------------------------------------------
#                          Range
#----------------------------------------------------------------
range(0,10)
print(list(range(10)))

print(list(range(2,20,2))) # Start stop ,step 

#=====================================================================================================#
#-------------
#Type Casting : - 
#--------------
# it is Process that convert the one data type into the another like : '123' string to int 123

#----------------------
# Implicit type casting:-
#----------------------
# It is convereted automatically by the the python into a comptable data type 
# which coverets int to float not string to int.

#-------------------------- 
#2).Explicit Type casting : -
#--------------------------
# This is done by the python function like : str(),: str(111)= '111', float() , int(2.05)

#===================================================================================================#

#--------------------------
#Other data type functions: - 
#--------------------------

# ord(): integer into the underlying  unicode representative character ,
# hex(): converts integer to hexa decimal string , 
# oct() : 

#==================================================================================================#
#-------------------------------------------
# Python's User control input and formating:
#-------------------------------------------

#1.) String concatenation  and Direct Fromating with print()

print("I like {0} more than the {1}".format("orange","mango"))

#2.) Input / Output formating 
str1=input("please inter your first name ")
str2=input("please enter your last name ")
print("hello" +" "+ str1+ ' '+str2)

#=====================================================================================================#

print([[i+j for i in "abc"] for j in "def"])

# Difference Between the Sequence and Collection Data Types 
'''
--Order
Sequences maintain a specific order of elements.
Collections may or may not maintain order.
For example, dictionaries and sets are collections that do not maintain order.

-- Indexing:

Sequences allow indexing and slicing.
Not all collections support indexing. For example, sets do not allow indexing.

-- Mutability:

Some sequences are mutable (like lists) and some are immutable (like tuples and strings).
Collections also have both mutable (like lists and dictionaries) and immutable types (like frozensets).
'''