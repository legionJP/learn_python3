

#Closures: 
'''

# A Closure is a record storing a function together with an environment .

An environment is a mapping associating each free varriable of the function with the value 
or storage location to which the name was bound when the closure was created . A closure , 
unlike a plain func , allows the func to access those captured variables through the closure's 
refrence to them , even when the function is invoked outdsid etheir sope 

'''


def outer_func():
    message = 'Hi, You '

    def inner_func():
        print(message) # it is called the free variable  

    #return inner_func()
    return inner_func
     
#outer_func()
my_functon = outer_func()  #my_function is a function that is equal to the inner_func , bcz outer_func is returning this 

print(my_functon) #inner function adress 

my_functon()  
my_functon() 
my_functon()

# inner_function still has the access to the message variable which we are  returning 
# So a closure is an inner function that remember and has access to the variiable and
#the local scope in which it is created even after the outer func finishe excecuting 

def outer_func1(msg1):
    message = msg1

    def inner_func():
        print(message) # it is called the free variable  

    #return inner_func()
    return inner_func
     
my_functon1 = outer_func1('Hi I am first')
my_functon2 = outer_func1('Hello I am second') 
#my_function is a function that is equal to the inner_func ,bcz outer_func is returning this 
my_functon1() #it is fun with no para or argument
my_functon2()

print(my_functon1) #inner function adress 


#---------------------------------------------------------------------------
#Examples : 3 # Logging 

import logging

logging.basicConfig(filename='example.log',level=logging.INFO)

def logger2(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return logger2

def add(x ,y):
    return x+y
def subtract(x,y):
    return x-y

add_logger = logger2(add)
sub_logger = logger2(subtract)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(12,5)


