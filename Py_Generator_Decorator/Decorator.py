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
    def wrapper_function():
        return original_function()   #This is decorator 
        #print(message)
    return wrapper_function

hi_func = outer_fun('Hi')
bye_func = outer_fun('Bye')

hi_func()
bye_func()