#-----------------------------------------------------------------------------------------------------------------#
#                      2. Polymorphism :
#------------------------------------------------------------------------------------------------------------------#

# In this the object  can have or can be in the multiple forms .
# usages
# Loose coupling # 2. Dependency injection  # Interfaces 

#------------------------------------------------------------------------------------------------------------------#
#                Types of the Polymorphism:
#------------------------------------------------------------------------------------------------------------------#
# 1. Duck Typing  #2. Operator Overloading  #3. Method Over Loading  #4. Method Overriding

'''
Ability of a function to change it's behaviour when it's called by differnet objects 
example : built in "+" operator perform the additon
 for the integer data tuple and concation for the string data type
'''

# Everything in Python is inherently an object, so when I talk about polymorphism, 
# it can be an operator, method or any object of some class.

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
# used the same operator () to perform on a string, integer and a list. You can see the () operator behaves differently in all three cases.

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

#The len() function is able to take variable inputs. In the example above it is a string and a list that provides the output in integer format.
