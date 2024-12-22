#Argument for decorator or customizeable layer to decorator 

def prefix_decorator(prefix):
   
    def decorator_fun(origi_func):
       def wrapper_fun(*args,**kwargs):
           print(prefix,'Executeed before',origi_func.__name__)
           result = origi_func(*args, **kwargs)
           print(prefix,'Execcuted after ', origi_func.__name__ ,'\n')
           return result
       return wrapper_fun
    return decorator_fun
      
     
@prefix_decorator('Texting Log:')        #in this decoraotr we can pass on the our argument 
def display_fun(name,age):
   print('display info ran with ({}, {})'.format(name,age))

display_fun('JP', 24)
display_fun('vK', 23)




