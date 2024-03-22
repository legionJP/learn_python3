from typing import Any


def outer_fun(msg):
   # message = msg

    def inner_function():
        print(msg)
    return inner_function

#my_func=outer_fun() 
func1 = outer_fun('First')
func2 = outer_fun('Second')

func1()
func2()

#Decorator 
'''
It is just a function that takes another function as a argument and 
add some kind of functionality and then return other function without altering the source code 
'''

def decorater_fun(original_function):
    def wrapper_function(*args,**kwargs):
        print('Wrapper is  excecuting before the  {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)   #This is decorator 
        #print(message)
    return wrapper_function

# def display():
#     print("Display func ran")
# decorater_display = decorater_fun(display)
# decorater_display() #Equal to the wrapper function 

#=-----------------------------------------------------------------------------------
#decorator expression type = " @decorater_fun = decorator_display = decorator_fun(display) are the same"
#------------------------------------------------------------------------------------

# or Using the Function as a Decorator with multiple func 


@decorater_fun
def display():
    print("Display func ran")
#display()

@decorater_fun
def display_info(name ,age):
    print('The info about person name and age is ({} ,{})'.format(name,age))
display_info('Jay',23) 

display()
 
#-----------------------------------------------------------------------------------
 #Using the Classes as a Decorator


def decorater_fun1(original_function1):
    def wrapper_function1(*args,**kwargs):
        print('This is excecuting before the wrapper {}'.format(original_function1.__name__))
        return original_function1(*args,**kwargs)   #This is decorator 
        #print(message)
    return wrapper_function1

class decorator_class(object):
    def __init__(self,original_function1):   #passing the original fun in class
        self.original_function1 = original_function1
         
#mimicking the functionality by call method 
        
    def __call__(self, *args, **kwargs): 
        print('Call method executed this before the  {}'.format(self.original_function1.__name__))
        return self.original_function1(*args,**kwargs)  # WE are using the instance method here   

@decorator_class
def display1():
    print('Display1 func ran ')

@decorator_class
def display1_info(name,age):
    print('Display 1 info ran with the arguments ({},{})'.format(name,age))

display1_info('Josh', 19)

display1()
 
#-------------------------------------------------------------------------------------------------------
#Examples of the Decoraotr
#------------------------------------------------------------------------------------

#Logging function

def my_logger(original_function2):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function2.__name__), level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return original_function2(*args,**kwargs)
    return wrapper

def my_timer(original_function2):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function2(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in the :{}sec'.format(original_function2.__name__,t2))

        return result
    return wrapper
