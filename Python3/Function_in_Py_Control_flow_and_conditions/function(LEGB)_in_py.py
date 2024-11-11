#function: it is a modular piece of code that can be use repeatedly 
#Function Syntax:  def<function name>(<params>):
                       #<task to complete>  \
#Exam: def sum(x:y):
           #return x+y

#  definifng and calling of the function

def hellofun():
    print('hello function')
     #task
    return 'this is me'
hellofun()
print(hellofun())
print(hellofun().capitalize) # you can the argument to the func
#  DRY concepts applied for the functios meana Dont Reapeat Yourself 


def calculate_tax(bill,tax_rate):
    return round((bill*tax_rate)/100.00,2) #precision to 2 decimal point 
print('total  tax of the bill is ',calculate_tax(123,10))
print('total tax on the bill 1234 and tax rate 10 will be',calculate_tax(123,5))


# Leap Year code and days in Month 

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
#--------------------------------------------------------------------# 
# Varriable Scope in py 
#--------------------------------------------------------------------#

# 4 types of Scope 'LEGB' 1. Local 2. Enclosing Scope 3. Global 4. Built in 
# 1. Built in Scope or def() : function defining 
def outer():
    #2 Enclosed Scope
    b=2              #Accessible in:  Local and Enclosed Scope 
    def inner():
        #3. local Scope
        c=3           #Accessible in: only Local Scope 

   #4. Global Scope: function declared outside of a function , can be accessed from anywherer  
        #Examples:

def outer_1():
    x='outer x1'
    def inner_1():
       # x= 'inner x'
        inner_1()
        print(x) #printing the enclosed  scope value x1 
outer()        

#-----------------------------------------------------------------------

my_global=10
x='global v'
def fun1():
    global v #now we can print this within fun as global scope
    local_v =5
    print('Access to/print global',my_global)
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
    