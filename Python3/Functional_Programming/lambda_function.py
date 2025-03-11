#--------------------------------------------------------------------------------------------------#
#                           Lambda or Anonymous Function
#--------------------------------------------------------------------------------------------------#

# function is created using the def and when the function name is not mentioned than the fucntion is 
# anonymous and we call it anonymous function or Lambda
# 
def sqr(a):
    result = a*a
    return result
print(sqr(5))


#--------------------------------------------------------------------------------------------------#
#                                              Lambda
#--------------------------------------------------------------------------------------------------#
# When we want to use the function only once without defining the name of it
# We can pass function to a function because functions are object in the python

# function without defining it
f=lambda a: a*a      # here a is argumnet and a*a is operation on the argument, lambda is keyword and function
# is assign to f so f represents the function
print(f(25))

#2.
f2 = lambda a,b: a+b    # It can have the number of arguments but should have one expression like a+b or a-b
print(f2(23,45))
#--------------------------------------------------------------------------------------------------#

