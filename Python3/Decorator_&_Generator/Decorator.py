#=-------------------------------------------------------------------------------------#
#                             Decorator 
#----------------------------------------------------------------------------------------#
'''
It is just a function that takes another function as a argument and add some kind of 
functionality in func and then return other function without altering the source code or the function
'''
#decorator expression type 

def super_secret_function(f):
    return f

@super_secret_function
def my_function():    # here the my_function is arg for the super_secret_func and super return the arg func
    print("This is my function")

# Herer The @-notation is syntactic sugar that is equivalent to the following:
my_function = super_secret_function(my_function)

#---------------------------------------------------------------------------------------------#

# Example: 1. 

def div(a,b):
    print(a/b)  # want function to always divide  greater number

#div(2,4)

def smart_dev(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner    

div1 = smart_dev(div)
print(div1(3,9))

#---------------------------------------------------------------------------------------------#
# Examples- 2.
#-----------------------------------------------------------------------------------#

def decorater_fun(original_function):
    def wrapper_function(*args,**kwargs):
        print('Wrapper is  excecuting before the  {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)   #This is decorator 
        #print(message)
    return wrapper_function

# def display():
#     print("Display func ran")
# decorater_display = decorater_fun(display)   #The decorator defination
# decorater_display() #Equal to the wrapper function 

'''Note
@decorater_fun = decorator_display = decorator_fun(display) are the same"

'''
#---------------------------------------------------------------------------------------------#
# Examples- 2. 
#  Using the Function as a Decorator with multiple func 
#----------------------------------------------------------------------------------------------#

@decorater_fun
def display():
    print("Display func ran")
#display()

@decorater_fun
def display_info(name ,age):
    print('The info about person name and age is ({} ,{})'.format(name,age))
display_info('Jay',23) 

display()


#---------------------------------------------------------------------------------------------#
#        Using the Classes as a Decorator
#---------------------------------------------------------------------------------------------#

def decorater_fun1(original_function1):
    def wrapper_function1(*args,**kwargs):
        print('This is excecuting before the wrapper {}'.format(original_function1.__name__))
        return original_function1(*args,**kwargs)   #This is decorator 
        #print(message)
    return wrapper_function1

class decorator_class(object):               #The base class of the class hierarchy,When called, it accepts no arguments and returns a new featureless instance that has no instance attributes and cannot be given any.
    def __init__(self,original_function1):   #passing the original fun in class
        self.original_function1 = original_function1
         
#mimicking the functionality by call method 
        
    def __call__(self, *args, **kwargs): 
        print('Call method executed this before the  {}'.format(self.original_function1.__name__))
        re#-----------------------------------------------------------------------------------------------------#turn self.original_function1(*args,**kwargs)  # WE are using the instance method here   

@decorator_class
def display1():
    print('Display1 func ran ')

@decorator_class
def display1_info(name,age):
    print('Display 1 info ran with the arguments ({},{})'.format(name,age))

display1_info('Josh', 19)
display1()

 
#-------------------------------------------------------------------------------------------------------
#                                   Examples of the Decoraotr
#------------------------------------------------------------------------------------------------------#


#1.  Logging function
#-------------------------------
from functools import wraps  # for using the decorator inside of decorator

def my_logger(original_function2):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function2.__name__), level=logging.INFO)
    
    @wraps(original_function2)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return original_function2(*args,**kwargs)
    return wrapper

@my_logger
def display_info1(name,age):
    print('Display info ran with the argumetns ({}, {})'.format(name,age))

display_info1('Ash',32)

#--------------------------------------------------------------------------------------
#                           2. Timmer Function
#---------------------------------------------------------------------------------------

def my_timer(original_function2):
    import time
     
    @wraps(original_function2)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function2(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in the :{}sec'.format(original_function2.__name__,t2))

        return result
    return wrapper  #this allows to added the functionality to original_func2

import time
@my_timer
def display_info2(name,age):
    time.sleep(2)
    print('display_info2 ran with the arguments ({}, {})'.format(name,age))

display_info2('AK',23)  

#-------------------------------------------------------------------------------------------------------------------------#-
#                          3. Using the both function 
#-----------------------------------------------------------------------------------------------------#

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display info ran with the argument ({}, {})'.format(name,age))

#display_info =my_logger(my_timer(display_info)) #here we passing my_wrapper fun to logger and the originl_fun is not equal to this functon but equal to this wrap fun in timer thats why retruning the wrap log 
#display_info= my_timer(display_info)
print(display_info.__name__)

display_info('Mark',29)    

#-----------------------------------------------------------------------------------------------------#
'''
Note:

#Preserving the information of the original function whenever using the decorator
#Using the functool module and wrap decorator
#from functools import wraps # at the top
'''


