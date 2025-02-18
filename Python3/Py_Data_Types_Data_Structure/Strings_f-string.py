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
