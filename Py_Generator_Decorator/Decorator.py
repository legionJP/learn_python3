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
add some kind of functionality and then return other function without altering thesource code 
'''

def decorater_fun(original_function):
    def wrapper_function(*args,**kwargs):
        print('This is excecuting before the wrapper {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)   #This is decorator 
        #print(message)
    return wrapper_function

# def display():
#     print("Display func ran")
# decorater_display = decorater_fun(display)
# decorater_display() #Equal to the wrapper function 

#Decorator expression type = " @decorater_fun = decorator_display = decorator_fun(display) are the same"

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
 

 #Using the Classes as aDecorator