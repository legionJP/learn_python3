#-----------------------------------------------------------------------------------------------------------------#
#                      2. Polymorphism :
#------------------------------------------------------------------------------------------------------------------#

# In this the object  can have or can be in the multiple forms .
# usages
# Loose coupling # 2. Dependency injection  # Interfaces 

#------------------------------------------------------------------------------------------------------------------#
#                Types of the Polymorphism:
#------------------------------------------------------------------------------------------------------------------#
# 1. Duck Typing  #2. Operator Overloading  #3. Method Over Loading  #4. Method Overriding

'''
Ability of a function to change it's behaviour when it's called by differnet objects 
example : built in "+" operator perform the additon
 for the integer data tuple and concation for the string data type
'''

# Everything in Python is inherently an object, so when I talk about polymorphism, 
# it can be an operator, method or any object of some class.

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
# used the same operator () to perform on a string, integer and a list.
#  You can see the () operator behaves differently in all three cases.

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

#The len() function is able to take variable inputs.
# In the example above it is a string and a list that provides the output in integer format.

#------------------------------------------------------------------------------------------------------------------#
#                                1.   Duck Typing
#------------------------------------------------------------------------------------------------------------------#

'''
Duck typing and Easier to ask forgiveness than permission(EAFP)
Duck typing means object walk like duck and quacks like duck 
>> Means what types of object it is doesn't matter, it should _do__ what is ask to do 
'''

#Dynamic typing = mention or assign later
x= 'myname' # Type of myname of x is str
# In Python, self refers to the instance calling the method. 
# When you define a method in a class, the instance (object) 
# calling the method is automatically passed as the first argument, 
# which is conventionally named self.

#------------------------------------------------------------------------------------------------------------------#
# Example 1:
#------------------------------------------------------------------------------------------------------------------#

class VimEdtior:
    def execute(self):
        print("It is better than every other")
        print("Can compile!")
        print("can run code !")

class Vscode:
    def execute(self):
        print("compiling")
        print("Running")

class Laptop:
    def code(self,ide): #take the arg of ide and func for the ide is Vscode
        ide.execute()  #ide will be dynamic where the object have the execute method

# Here the ide is the object which have the method 'execute' and 
# it is behaving like a duck  bcz it only need the execute method , class don't matter
# so it is called  the Duck Typing , because as a polymorphism the object is having multiple behaviour or 

lap1= Laptop() 
ide1 = VimEdtior()
lap1.code(ide1)

lap2 = Laptop()
ide2 = Vscode()
lap2.code(ide2)

 # above is creating the instance of class ide1, means the ide1 is object and has the 
# acess to the methods inside the class

ide1 = Vscode()
 # ide1 is assigning the class to the ide1 if we put it like thos : ide1 = Vscode  
lap1.code(ide1)


#------------------------------------------------------------------------------------------------------------------#
#                                2.   Operator Overloading
#------------------------------------------------------------------------------------------------------------------#

'''
5+6 ----> 5, 6 operands and + is operator
>>  
'''

a= 5
b= 'world'
#print(a+b)

# it is unsupported operand bcz it is predefined and 
#it is called the synthetic sugar - means simplify the code for the user

b=7
print(a+b) # or
print(int.__add__(a,b))  # so behind the scene the add is int class method and getting called 

a='t1'
b='t2'
print(str.__add__(a,b))

'''
>> so there is different method for the different operator and these are called the magic methods
1. + == __add__()
2. - == __su__()
3. * == __mul__()
'''

class Students:
    def __init__(self,m1,m2) -> None:
        self.m1 =m1
        self.m2 =m2

    #step2
    def __add__(self,other):
        m1 = self.m1+other.m1
        m2= self.m2 +other.m1

        s3 = Students(m1,m2)
        return s3    
    #Step3/example3

    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>s2:                # So here s1 and s2 are the simple variable of int not the object
            return True
        else:
            return False
    # step4
    def __str__(self) -> str:
        return "{} {}".format(self.m1,self.m2)     # return the str value

        
s1 = Students(59,95)
s2 = Students(67,95)   

s3 = s1+s2  
#TypeError: unsupported operand type(s) for +: 'Students' and 'Students'

# here the method doesn't have the add method , so you have to overload  or define the method in students class
# But also students class don't know the plus method so we have to call the add method but don't have the add method
#so we have to define the add method here

#step2
print(s3.m1) # here the add method is called for m1 as  s3.m1 
print(s3.m1+s3.m2)
print(type(s3.m1)) # as the type of s3.m1 is int so we can add these object no bcz int knows the + operator 

if s1> s2:
    print("s1 is 1st")
else: 
    print("s2 is 1st ") # Again same error - TypeError: '>' not supported between instances of 'Students' and 'Students'

# So If you want to perform any operation on the the user defined object you have to define all of its method of operations

a=9
print(a)
print(s1) #calling the str
print(a.__str__())
print(s1.__str__())  # to avoid to print the object address and print the address we need to override the str method


# Note comment out step 2, 3, 4 when learning 1 by 1

#------------------------------------------------------------------------------------------------------------------#
#                                3. Method  Overloading
#------------------------------------------------------------------------------------------------------------------#

class Students:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 =m2

    #def sum(self,a,b):
    def sum(self, a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s= a+b+c
        elif a!=None and b!=None: 
            s=a+b
        else:
            s =a
        return s
    
    
s1 = Students(67,34)
print(s1.sum(67))    

'''
Here we defined a single sum method in the Students class, but with optional parameters. 
This allows the method to handle different numbers of arguments,
mimicking method overloading because the python does not support the overloading directly

'''        


#------------------------------------------------------------------------------------------------------------------#
#                                4. Method   Overriding
#------------------------------------------------------------------------------------------------------------------#

class A:
    def show(self):
        print("a show method ")

# class B(A):
#     pass        

class B(A):
    def show(self):
        print("B's show method")
        # return super().show()

a1=B()
a1.show()    

'''
1. When we don't have the method show in the class B and class B is inheriting A than the 
B is inheriting the A's show method ,
2.But when the B has it's own show method than it overrides 
the A's method 
'''
#------------------------------------------------------------------------------------------------------------------#
