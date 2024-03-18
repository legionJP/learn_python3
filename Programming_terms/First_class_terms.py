# First Class Function: 
''' A programming language is said to have first class functions if it treats 
    functions as first class citizens.
'''

#First Class Citizen (in Programming)
'''
"|A first class citizen (sometimes called first class objects) in a programming language 
is an entity which supports all the operations generally available in other entities.

These operations typically include being passed as a argument , returned from a 
functions and assigned to a varriable.
" # Means : Be will be able to treat a function as a anyother objects.
'''
# if fun  accepts other fun as fun or returns as a argument its called the higher order function

#Python program 

def square(x):
    return x * x
f = square # here we are not executing the code so we are not using the () , var x is equal to the x
#f= square(5)

print(square)
print(f)  #f , an fun square add is same , means we can use f inseat of square

print(f(5))

#Java Script Code

'''
function square(x){
     return x*X;
}

var f = square

console.log(square)
consloe.log(f)
consloe.log(f(5))

'''


# Map Function custom built in 

#Square func

def square(x):
    return x*x

#cube Function

def cube(x):
    return x*x*x

def my_map(func, arg_list):
    result =[]
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1,2,3,4, 5])

print(squares)

#Logger Function

def logger(msg):
     
     def log_message():
         print('Log:', msg)
     return log_message()                                                               

log_hi = logger('Hi') # this log_hi can be called as a functions 
# this log hi is equal to log_message function which logger func is returning 
log_hi()       

                    