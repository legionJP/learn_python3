# Duck typing and Easier to ask forgiveness than permission(EAFP)
# Duck typing means object walk like duck and quacks like duck means what types of object it is it should what is ask to do 


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

#Pythonic (#EAFP)
        
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
       # thing.bark()
    except AttributeError as e:
        print(e)

    print()

'''
  #Not duck type Non pythonic

def quack_and_fly(thing):
    #if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
   # else: 
       # print('This has to be duck!')
        print()
'''

 #LBYL Non pythonic 
'''
def quack_and_fly(thing):
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly() #run the method, asking in eveey method to do that
    print()  
'''
    
d = Duck()
quack_and_fly(d)

p= Person()
quack_and_fly(p)



# Examples

#person = {'name': 'Jay', 'age': 22 , 'job': 'Devloper'}
person = {'name': 'Jay', 'age': 22}

# LBYL (Non Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'am  {age} years old and I am a {job}".format(**person))
else:
    print("Missing some words")


#EAFP Pythonic
    
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
#    in pythonic accessing the object one time 

 #########################################################################################################

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


