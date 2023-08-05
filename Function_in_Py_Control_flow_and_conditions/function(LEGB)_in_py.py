#function: it is a modular piece of code that can be use repeatedly 
#Function Syntax:  def<function name>(<params>):
                       #<task to complete>  \
#Exam: def sum(x:y):
           #return x+y

def calculate_tax(bill,tax_rate):
    return round((bill*tax_rate)/100.00,2) #precision to 2 decimal point 
print('total  tax of the bill is ',calculate_tax(123,10))
print('total tax on the bill 1234 and tax rate 10 will be',calculate_tax(123,5))

#Varriable Scope in py 

#4 types of Scope 'LEGB' 1. Local 2. Enclosing Scope 3. Global 4. Built in 
#1. Built in Scope or def() : function defining 
def outer():
    #Enclosed Scope
    b=2              #Accessible in:  Local and Enclosed Scope 
    def inner():
        #local Scope
        c=3           #Accessible in: only Local Scope 

   #Global Scope: function declared outside of a function , can be accessed from anywherer  
my_global=10
def fun1():
    local_v =5
    print('Access to global',my_global)
    def fun2():
        local_v2=local_v*2
        print(my_global)
        print(local_v)
    fun2()
    return local_v
fun1()
#return my_global


  # Here callingg the  function outside of the fun.  which have the globle print the varriable
#print('cant access the local value ',local_v) #so the varraibel cant be acceesd outside of the function


#2.) Loacal Scope: it can be only used inside the declaredd function , 
#3). Enclosing Scope: It is the varriable which can be used inside the another function or with the nested function
#4).Built in Scope: these are the reserved keywords that python uses for built in function : print , def ,for etc.

my_global=10
def fun11():
    enclosed_v=12
    def fun21():
        local_v =5
        print('Access to global',local_v)
        print('this is the enclosed var',enclosed_v)
        fun21()
fun11()     