#---------------------------------------------------------------------------------------
# String Operations
#---------------------------------------------------------------------------------------
message ="Hello my World"
print(message)
print(len(message))
print(message[2])
print(message[0:6]) 
print(message.count('l'))
print(message.count('World')) # counting the string chracter

#---------------------------------------------------------------------------------------
# Find the string character using the String find method
#---------------------------------------------------------------------------------------

print(message.find('Jp'))  #the ouput is 6 because the word is strating from the index 6
print(message.find('y'))

#---------------------------------------------------------------------------------------
# Replacing  method for the String 
#---------------------------------------------------------------------------------------
message=message.replace('Hello' , 'Welcome')
print(message)

#--------------------------------------------------------------------------------------
# Cocatinatong the string
#--------------------------------------------------------------------------------------

greeting = "hello"
name = 'JP'
message = greeting + ',' + name + ' welcome '
print(message)

#--------------------------------------------------------------------------------------
# String .join method
#--------------------------------------------------------------------------------------
str_list = ["Hello", "world"]
result = " ".join(str_list)
print(result)


#--------------------------------------------------------------------------------------
# String formating 

message= '{}, {} welcome'.format(greeting,name)
print(message)

#---------------------------------------------------------------------------------------

# f-string fromating
#---------------------------------------------------------------------------------------
message= f'{greeting}, {name.upper()}.Welcome!'
print(message)

#Find out the help about the methods and attributes of the string and funtion 

print(dir(name))
print(help(str))

#---------------------------------------------------------------------------------------------------
# String Formating for Dictionary
#---------------------------------------------------------------------------------------
person ={'name': 'jenn', 'age': 23}
sentence = 'My name is '+ person['name'] + ' and I am ' + str(person['age']) +' years old' 
print(sentence)

person = {'name': 'jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old'.format(name=person['name'], age=person['age'])
print(sentence)


#---------------------------------------------------------------------------------------
# by using the  String .format method

sentence= "My name is  {0} and I am {1} years old ".format(person['name'],person['age'])
sentence2= 'My name is  {0[name]} and I am {1[age]} years old '.format(person,person)
sentence3= 'My name is  {0[name]} and I am {0[age]} years old '.format(person) 
# in the case of the list we can also provide the index no like 0 , 1 in the place of the name , age

print(sentence)
print(sentence2)
print(sentence3)

#-----------------------------------------------------------------------------------------
#2. Using the string formation by format method
##-------------------------------------------------------------------------------------#

tag ='H1'
name ='text type H1'
sentence= '<{0}> {1} </{0}>'.format(tag,name)
print(sentence)

##-------------------------------------------------------------------------------------#
class person():
    def __init__(self,name,age) -> None:
        self.name =name
        self.age= age
p1= person('Jack','83') #p1 is the instance of the class
sentence4='My name is {0.name} and I am {0.age} years old '.format(p1)

# 4. using the attribute
# by paasing the keywoord value
sentence5= 'My name is {name} and I am {age} years old '.format(name='John', age='30')
 
print(sentence5)
print(sentence4)

#----------------------------------------------------------------------------------------------
# String formating for the list unpacking
#----------------------------------------------------------------------------------------------

person1= {'name': 'Jenn','age': 23}
sentence ='My name is {name} and I am {age} years old'.format(**person1) # **kwargs
print(sentence)

#-------------------------------------------------------------------------------------------

# Numbers formatiing by using the place holders {}

for i in range(6,12):
    Numbers='the value is {}'.format(i)
    Numbers1 ='The value is {:02}'.format(i)
    #print(Numbers)
    print(Numbers1)

pi=3.1459265
pie_value='The pi value to 2 digit is {:.2f}'.format(pi)
print(pie_value)

sentence6='1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence6)

#---------------------------------------------------------------------------------------------
# Fromating the Date and time
#---------------------------------------------------------------------------------------------
import datetime
my_date =datetime.datetime(2016,9,24,12,30,12)
print(my_date)

sentence6 = '{:%B %d, %Y}'.format(my_date)
print(sentence6) #%B is for the Month , and %d for the date , and %Y for the year

# for ' March -1 , 2016 fell on a 'tuesday' and was the '61' day of the year'

sentecne7= '{0:%B %d , %Y } fell on {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentecne7)

#---------------------------------------------------------------------------------------------

# Python String Methods
#---------------------------------------------------------------------------------------------

string = "Hello, World!"

# Length of a string
length = len(string)
print("Length of the string:", length)

# Convert string to lowercase
lowercase = string.lower()
print("The string in lowercase:", lowercase)

# Convert string to uppercase
uppercase = string.upper()
print("The string in uppercase:", uppercase)

# Capitalize the string
capitalized = string.capitalize()
print("Capitalized string:", capitalized)

# Convert the first character of each word to uppercase
title_case = string.title()
print("The string in title case:", title_case)

# Count occurrences of a substring
count = string.count("o")
print("Count of 'o':", count)

# Replace a substring
replaced = string.replace("World", "Unstop")
print("Replaced string:", replaced)

# Split the string into a list
split_list = string.split(",")
print("Split string:", split_list)

# Join elements of a list into a string
joined = "-".join(split_list)
print("Joined string:", joined)

# Strip leading and trailing whitespace
string2 = " Hello, World "
stripped = string2.strip()
print("Stripped string:", stripped)

multiline_string = "Line 1\nLine 2\nLine 3"
print(multiline_string)

# Using the splitlines(), startswith(), and endswith() functions
splitlines_list = multiline_string.splitlines()
print("Splitlines list:", splitlines_list)
print("Starts with 'Line':", multiline_string.startswith("Line"))
print("Ends with '3':", multiline_string.endswith("3"))

# Using the count() function
text = "Hello, Hello, Hello"
count = text.count("Hello")
print("Count of 'Hello':", count)

# using removeprefix() and removesuffix() functions
prefixed_string = "Prefix Hello, World!"
removed_prefix = prefixed_string.removeprefix("Prefix")
print("Removed prefix:", removed_prefix)

suffixed_string = "Hello, World! Suffix"
removed_suffix = suffixed_string.removesuffix("Suffix")
print("Removed suffix:", removed_suffix)

#---------------------------------------------------------------------------------------------

# Escape Characters & Python Strings : see ref String_Methods.md
#---------------------------------------------------------------------------------------------

# Newline 
print("Hello,\nWorld!")

# Tab 
print("Python\tProgrammingLanguage")

# Single and double quotes
print('Single Quote: \', Double Quote: \" ')

# Unicode characters
print("Unicode: \u03A9") # Represents the Greek capital letter omega

# Bell sound
print("Beep!\a")

# Hexadecimal value
print("Hex: \x48\x65\x6C\x6C\x6F") # Represents the ASCII values for "Hello"

#---------------------------------------------------------------------------------------------
# Summary:

"""
How to Format a String in Python?

1. Interpolation Operator (%)
   name = 'JP'
   string = 'Hello, %s!' % (name)

2. .format Method
   name = 'JP'
   string = 'Hello, {}!'.format(name)

3. f-String
   name = 'JP'
   string = f'Hello, {name}!'

print(string)
"""
"""
String Methods in Python
( Not see the Strings_Method.md file)

Function Name     | Description/Purpose                                            | Example
------------------|---------------------------------------------------------------|-----------------------------------------------------------------
len()             | Returns the length of the string                              | len("Hello") This returns 5
lower()           | Converts the string to lowercase                              | "Hello".lower() This returns "hello"
upper()           | Converts the string to uppercase                              | "Hello".upper() This returns "HELLO"
capitalize()      | Capitalizes the first character of the first word in a string | "hello".capitalize() This returns "Hello"
title()           | Capitalizes the first character of each word in the string    | "hello world".title() This returns "Hello World"
count()           | Returns the number of occurrences of a substring              | "Hello, Hello, Hello".count("Hello") This returns 3
replace()         | Replaces a substring (and all its copies) with another substring | "Hello, World".replace("Hello", "Hi") This returns, "Hi, World"
split()           | Splits the string into a list of substrings. By default, breaks the string wherever there is a whitespace. | "Hello, World".split(",") This returns ['Hello', ' World']
join()            | Joins elements of a list into a string using a separator.     | ", ".join(['Apple', 'Banana', 'Orange']) This returns "Apple, Banana, Orange"
strip()           | Removes leading and trailing whitespace                       | " Hello ".strip() This returns "Hello"
splitlines()      | Splits a multiline string into a list of lines/strings        | multi_line = "Apple\nBanana\nOrange"\nSplit_list = multi_line.splitlines() This returns a list of individual strings.
startswith()      | Check if the string starts with a given string/character digit | str1 = "How are you doing?"\nprint("Starts with 'How':", str1.startswith('How')) The result will be True.
endswith()        | Check if the string ends with a given string/character digit  | str1 = "How are you doing?"\nprint("Ends with '?':", str1.endswith('?')) The result will be True.
removeprefix()    | Removes a given prefix from the string                        | str2 = "Please, will you do this??"\nstr2_prefix = str2.removeprefix("Please, ") This will remove "Please" and space from the string.
removesuffix()    | Removes a given suffix from the string                        | str2 = "Will you do this??"\nstr2_suffix = str2.removesuffix("?") This will remove one question mark.
"""
