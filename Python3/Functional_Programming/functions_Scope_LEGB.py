
#---------------------------------------------------------------------------------------------------#
#                    Variable Scope in python Functions
#---------------------------------------------------------------------------------------------------#

# Namespace: it is the container where the names are mapped to the objects

# Ther is 4 Types of Scope 'LEGB' 1. Local 2. Enclosing Scope 3. Global 4. Built in 

# 1. Built in Scope or def() : function defining 
def outer():
    #2 Enclosed Scope
    b=2              #Accessible in:  Local and Enclosed Scope 
    def inner():
        #3. local Scope
        c=3           #Accessible in: only Local Scope 

   #4. Global Scope: var declared outside of a function , can be accessed from anywherer  
'''
# Local Scope or Local Namespace:

The local namespace in Python refers to the scope that contains names (variables, functions, etc.)
defined within a function. Every time a function is called,
a new local namespace is created for that function's execution context.    

# 2. Enclosing Namespace In Python

When an inner function accesses a variable that is not defined locally but is in the scope of an outer function, 
it accesses the enclosing/ immediate outer namespace.

It is important to note that while the inner function can access the variables from its enclosing Python namespace, 
it cannot modify the value without the use of the nonlocal keyword. 

# 3. Global Namespace In Python
Global (G) Scope: Variables defined at the top level of a module or declared as global 
within a function are considered global. They are accessible throughout the module. 
Global variables persist until the interpreter terminates or until they are explicitly deleted.

# 4. Built-in Namespace In Python
Built-in (B) Scope: Python's built-in namespace contains names like print(), len(), etc.
 These names are always accessible from any scope without any import statements.
'''


# The globals() Function
'''
The built-in function globals() returns a dictionary representing the current global namespace.
That is, when you call this function, it will return all entries in global namespace. 
This includes, all variables and functions defined at the top level of a module or script, 
even including variables from imported modules.
'''
# Global variable
global_var = 'I am global'

def my_function():
  local_var = 'I am local'
  print("Inside function - Global namespace:")
  print(globals())

# Call the function
my_function()

# Access global_var directly using globals()
print("Global variable accessed directly:", globals()['global_var'])

#---------------------------------------------------------------------------------------------------#
#Examples:
#1. 

b=9
a= 10
c = 7
def scope_fun():
    global b  # here mentioning b explicitly as global so it is same as outide and inside func scope
    b=11  
    a= 15 # we can't use the same name var if it  defined as global
    print("insider a ",a)
    print("insider b ",b) # as b=9 but inside gloabal b=11 so it print 11 bcz prefence is given to inside vars.
    print("global is accessed inside func c: ", c)
    x = globals()['a']
    print(x)
    print(id(x)) 
    #globals()['a']= 11 # Here change the gloabl var without affecting the local variable

scope_fun()
print("outsider a ",a) # it will print the 10 not 15 bcz you can't access the inside var means local var outside
print("b as a outside ",b)
print(id(a)) # the add is same for global a and x 

#---------------------------------------------------------------------------------------------------#
#2. 
def outer_1():
    x='outer x1'
    def inner_1():
       # x= 'inner x'
        inner_1()
        print(x) #printing the enclosed  scope value x1 
outer_1()        

#------------------------------------------------------------------------------------------------#

my_global=10
x='global v'
def fun1():
    global v #now we can print this within fun as global scope
    local_v =5
    print('Access to /print global',my_global)
    def fun2():
        local_v2=local_v*2
        print(my_global) #GLOBAL
        print(local_v2) #Enclosed
        print(local_v) #local
    fun2()
    #print(local_v) , mae error when !!
    return local_v  #What is this return doing?
 
   #return my_global
fun1()
print(x)


# Here callingg the  function outside of the fun.  which have the globle print the varriable
#print('cant access the local value ',local_v) #so the varraibel cant be acceesd outside of the function


#2.) Loacal Scope: it can be only used inside the declaredd function , 
#3). Enclosing Scope: It is the varriable which can be used inside the another function or with the nested function

#-------------------------------------------------------------------------------------------------------------
#4).Built in Scope: these are the reserved keywords that python uses for built in function : print , def ,for etc.
'''
def min():
    pass '''

m = min([1,3,5,6,7,89,]) #builtin varriable
print(m)
import builtins
print(dir(builtins))


#------------------------------------------------------------------------------------------------------------------

#my_global=10
def fun_1():
    enclosed_v=12
    #print(z)
    def fun21():
        local_v2 =5
        print('Access to global',local_v2)
        print('this is the enclosed var',enclosed_v)
        
        fun21()
fun_1()



#--------------------------------------------------------------------------------------------------#
#                                            Function
#--------------------------------------------------------------------------------------------------#
'''
#Function: it is a modular piece of code that can be use repeatedly 
#Function Syntax:  def<function name>(<params>):
                       #<task to complete>  
'''
                      
def sum(x,y):
    return x+y
#  definifng and calling of the function

def hellofun():
    print('hello function')
     #task
    return 'this is me'
hellofun()
print(hellofun())
print(hellofun().capitalize) # you can the argument to the func
#  DRY concepts applied for the functios meana Dont Reapeat Yourself 

#--------------------------------------------------------------------------------------------------#
def calculate_tax(bill,tax_rate):
    return round((bill*tax_rate)/100.00,2) #precision to 2 decimal point 
print('total  tax of the bill is ',calculate_tax(123,10))
print('total tax on the bill 123 and tax rate 5 will be',calculate_tax(123,5))

#--------------------------------------------------------------------------------------------------#
#        Leap Year code and days in Month 
#--------------------------------------------------------------------------------------------------#
month_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    return year%4 ==0 and (year % 100 != 0 or year % 400 ==0)
def days_in_month(year,month):
    if not 1 <= month <=12:
        return 'Invalid Month'
    if month ==2 and leap_year(year):
        return 29
    return month_days[month]
print(days_in_month(2016,2))
print(leap_year(2016))
#--------------------------------------------------------------------------------------------------#