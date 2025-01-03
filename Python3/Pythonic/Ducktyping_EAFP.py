#------------------------------------------------------------------------------------------------------------------#
#                                   Duck Typing
#------------------------------------------------------------------------------------------------------------------#

'''
Duck typing and Easier to ask forgiveness than permission(EAFP)
Duck typing means object walk like duck and quacks like duck 
>> Means what types of object it is doesn't matter, it should _do__ what is ask to do 
'''

#Dynamic typing = mention or assign later
x= 'myname' # Type of myname of x is str
# In Python, self refers to the instance calling the method. 
# When you define a method in a class, the instance (object) 
# calling the method is automatically passed as the first argument, 
# which is conventionally named self.

#------------------------------------------------------------------------------------------------------------------#
# Example 1:
#------------------------------------------------------------------------------------------------------------------#

class VimEdtior:
    def execute(self):
        print("It is better than every other")
        print("Can compile!")
        print("can run code !")

class Vscode:
    def execute(self):
        print("compiling")
        print("Running")

class Laptop:
    def code(self,ide): #take the arg of ide and func for the ide is Vscode
        ide.execute()  #ide will be dynamic where the object have the execute method

# Here the ide is the object which have the method 'execute' and 
# it is behaving like a duck  bcz it only need the execute method , class don't matter
# so it is called  the Duck Typing , because as a polymorphism the object is having multiple behaviour or 

lap1= Laptop() 
ide1 = VimEdtior()
lap1.code(ide1)
 # above is creating the instance of class ide1, means the ide1 is object and has the 
# acess to the methods inside the class

ide1 = Vscode()
 # ide1 is assigning the class to the ide1 if we put it like thos : ide1 = Vscode  
lap1.code(ide1)

#------------------------------------------------------------------------------------------------------------------#
#    Example 2.
#------------------------------------------------------------------------------------------------------------------#
'''
Python follows the "duck typing" principle, which means that 
the type or class of an object is less important than the methods it defines. This 
allows you to create flexible functions and classes without explicitly defining templates.
'''

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck_like):
    duck_like.quack()

duck = Duck()
person = Person()

make_it_quack(duck)    # Quack!
make_it_quack(person)  # I'm quacking like a duck!

#------------------------------------------------------------------------------------------------------------------#

class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Person:
    def quack(self):
        print('I am Quacking like a duck')

    def fly(self):
        print('I\'m Flapping my Arms!')     
#------------------------------------------------------------------------------------------------------------------#
#1. Pythonic (#EAFP)

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
       # thing.bark()
    except AttributeError as e:
        print(e)

    print()

#------------------------------------------------------------------------------------------------------------------#
# 2. Not duck type Non pythonic:

def quack_and_fly(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else: 
        print('This has to be duck!')
        print()

#------------------------------------------------------------------------------------------------------------------#

 #LBYL Non pythonic 
#------------------------------------------------------------------------------------------------------------------#

def quack_and_fly(thing):
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly() #run the method, asking in eveey method to do that
    print()  

    
d = Duck()
quack_and_fly(d)

p= Person()
quack_and_fly(p)

#------------------------------------------------------------------------------------------------------------------#
#                      Examples:
#------------------------------------------------------------------------------------------------------------------#

#person = {'name': 'Jay', 'age': 22 , 'job': 'Devloper'}
person = {'name': 'Jay', 'age': 22}

# LBYL (Non Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'am  {age} years old and I am a {job}".format(**person))
else:
    print("Missing some words")

#------------------------------------------------------------------------------------------------------------------#
#                                   EAFP Pythonic:
#------------------------------------------------------------------------------------------------------------------#
    
try:
    print("I'm {name}. I'am  {age} years old and I am a {job}".format(**person))

except KeyError as e:
    print("Missing {} key".format(e))


my_lis = [1.,2,3,4,5]
 
if len(my_lis) >=6:
    print(my_lis[5])
else:
    print('This index does not exist')

 # Pythonic 
try:
    print(my_lis[5])
except IndexError:
    print("this index does not exit")


# when we try to access the object multiple times , then have to acess the objet multiple times 
#  in pythonic accessing the object one time 


#------------------------------------------------------------------------------------------------------------------#

import os 

my_file = '/Downloads/learn_python3/file1.txt'

# Race condition
if os.access(my_file,os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('file cant be accessed')


# No Race Condition 

try:
    f =open(my_file)
except IOError as e:
    print('file cant be accessed') 

else:
    with f:
        print(f.read())


#------------------------------------------------------------------------------------------------------------------#
