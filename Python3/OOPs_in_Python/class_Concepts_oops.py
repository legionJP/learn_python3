
#--------------------------------------------------------------------------------------------#
#                                    Programming paradigm-
#--------------------------------------------------------------------------------------#
# Programming paradigm are the strtagey for reducing the code complexity and determine the flow of the code 

'''
Type of the paradigm like: 
--------------------------
1. Declarative , Procedural , Object oriented , function , Logic  object , Event driven , flow driven 
---> In pyhton Paradigm follows , Object Oriented , Procedural and functional
'''
#--------------------------------------------------------------------------------------------#
#                             Object Oriented Programming 
#--------------------------------------------------------------------------------------------#
# OOP is  Resuable , Abstracrtion , Move between projects 

#--------------------------------------------------------------------------------------------#
#Key Components of the OOPS : CLASS, OBJECT
#--------------------------------------------------------------------------------------------#
#                                  1. Class  :
#--------------------------------------------------------------------------------------------#
'''
Class is a logical code blocks, it contains :  1. Attributes, 2. Behaviour:

1. Attributes : these can be a varriable: like data about object example- A person's height, company, age
2. Behaviour : behiour can be a function: Like action of the persons- walking, talking , any action

> We can create the instances of the classes called the object or
> class provide a blueprint for creating a object.
> Like class is the design and object is the it's stuff or instance.

'''
#-----------------------------------------------------------------------------------------------#
#                                  2. Object : 
#-----------------------------------------------------------------------------------------------# 
'''
Every object have the its attribute and behaviour
An attributes and Behaviour of the class define the state of the Object  :

>> (Object has something where you can store data(variables) and
it will have some behaviour(like methods or functions)). 

>> so if something need to store in object
we need to define a variales. and if want to define a behaviour we need to use a methods.
'''
#-------------------------------------------------------------------------------------------------#
# 3. Methods :  (It is function that is associate with class )
#-------------------------------------------------------------------------------------------------#
'''
Methods are the functions that are defined inside the class 
and determine the behviour of the object instances 
emp1.postion()   #calling the method

--> special method is : __init__
--> special Variables is : __name__
'''

#examples : 
#----------------------------------------------------------------------------------------------------------#
#                1.  Creating the object emp1  by calling the class employee()
#-----------------------------------------------------------------------------------------------------------#


class Computer:             # Put the attribute (variable) and behavour(method/functions) in the class
  def config(self):         # Methood
    print("i5, 8gb,1tb")

comp1 = Computer()   # comp1 object   of computer
print(type(comp1))

#Computer.config() # have to call the object of the class
Computer.config(comp1) # we are passing object as  parameter or argument 

comp1.config()  # using the object itself to call the method/func. ,config take the comp1 as a argument

#--------------------------------------------------------------------------------------------------------------#
#                                2. Class With Special Method: __init__
#--------------------------------------------------------------------------------------------------------------#
class Computer1:
   def __init__(self,cpu,ram):   # use the init to initialize the variables but  this also called constructor
      #pass
      self.cpu =cpu               # self.var =parameter
      self.ram = ram
      print("init")               # for every object it the init  get called one time 

   def config1(self):                     # here self is object itself, cpu and ram parameter is passed    
    print("config is ", self.cpu,self.ram)   # Here One Method have it's own varibale 

comp2= Computer1('i5','8GB')
comp3=Computer1('r5','16GB')
# comp2.config1('i5','4gb')
# comp3.config1('i9','16 gb')

#--------------------------------------------------------------------------------------------------------------#
# 3.
class employee:
    def position(self,position,emp_status):         
        return print( "I am a",emp_status,position)
    
#Object Creating OR Creating the instances of the class 
emp1 = employee()  
emp1.position("programmer ","active")
#-------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------#
#                                       Constructor and self
#-------------------------------------------------------------------------------------------------------------#

'''
SO Constructor will assign/calculate or alloacte the size of the object, 
constructor call the init method internally
'''

class Computer3:
    def __init__(self) -> None:
      self.name ="JP"
      self.age =22  # self point towards to the current instnace like self.age = c1 age when c1.age=23

    def compare(self,other):
       if self.age==other.age:
          return True
       else:
          return False
       
c1= Computer3() #object inside the heap memory and take some space
c1.age=30
c2 = Computer3() # size of the obj. depends onn the number of vars. passed ,

if c1.compare(c2):
   print("it's same")
else:
   print("they are same")   
print(id(c1)) # it will take every time the reference spaces
print(id(c2))
c2.name='JP'
print(c1.name)
print(c2.name)
#---------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------#
#                                      CLASS CONCEPT
#---------------------------------------------------------------------------------------------------------------#
#                            1. Instances of the classes
#---------------------------------------------------------------------------------------------------------------#
class Employee:  #class is the blueprint for creating the instances
   
   def __init__(self,first,last,pay): #first instance is self
        self.first =first      # this method called intialize and in other language  it called as constructer
        self.last = last
        self.epay =pay
        self.email = first + '.' + last + '@email.com'
        
   def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1= Employee('jp','pal',50000)
emp2 = Employee('name1','last',20000)
# print(emp1)
# print(emp2)
print(emp1.email)
print(emp2.email)

#---------------------------------------------------------------------------------------------------------------#
#                   Types of Variables: 1. Instance Variable 2. Class(static) variable
#---------------------------------------------------------------------- ----------------------------------------#

class car:
  wheels =4    # common to every obj these are static or class variable
  def __init__(self):
     self.mil =110
     self.com ="BMW" # Theses are instance var. bcz it changes
     '''
     When You define the var inside init it becomes the instance varibale 
     and variable outside init and inside class become class variable
     '''

c1=car()
c2=car()
c1.mil=8          # c1 instance var. value for c1 changes
print(c1.com,c1.mil) 
print(c2.com,c2.mil,c2.wheels) # calling class var. using it by object name

#---------------------------------------------------------------------------------------------------------------#
#                                           NameSpace :
#---------------------------------------------------------------------------------------------------------------#

'''
namspace is place where you create and store object/variable
1. Class namspace
2. Object/ instance space
'''
car.wheels =5 # so it is changed and affect all the objects/instance 


#---------------------------------------------------------------------------------------------------------------#
#           Types of Methods :  (It is function that is associate with class )
#---------------------------------------------------------------------------------------------------------------#
# 1. Instance Method 2. Class Methods
#---------------------------------------------------------------------------------------------------------------#

class Students:
  school= 'ITI'    # class var.
  def __init__(self,m1,m2,m3):
     self.m1 =m1
     self.m2 =m2
     self.m3 = m3   #m1,m2,m3 are instance vars.

# '''
#   Here the avg is instance method , bcz we are passing self and it belongs to object
#   Types of Instance Method:
#    1. Accessor method(To fetch the value of instnace)
#    2. Mutator Method(to modify the value)
# ''' 
  def avg(self):
    return (self.m1+self.m2+self.m3)/3 
  
  def get_m1(self):   # Getter or Accessor
    return self.m1

  def set_m1(self,value): # Setter or mutator
    self.m1 = value    

#---------------------------------------------------------------------------------------------#
# Class Method
#---------------------------------------------------------------------------------------------#

  @classmethod          # to covnvert func as class method- decorator
  def get_school(cls):  # Class Method
    return cls.school  
     
#---------------------------------------------------------------------------------------------#
# Static Method :  not concern about the instance var or class var.
#---------------------------------------------------------------------------------------------#

  @staticmethod
  def info():
    print("This is student class static method") 

#---------------------------------------------------------------------------------------------#
# Example class method

s1 = Students(23,34,21)
s2= Students(12,43,23)
print(s1.avg())
print(Students.get_school()) # class method work with class variables.
Students.info() # using the static method doing some extra with class


#--------------------------------------------------------------------------------------------------------------#
#                                   Inner Class
#--------------------------------------------------------------------------------------------------------------#

class Students:
  def __init__(self, name, rollno) -> None:
    self.name =name
    self.rollno = rollno
    self.lap= self.Laptop() # You can create the object of inner class inside the outer class

  def show(self):
    print(self.name, self.rollno)
    self.lap.show() 

  class Laptop:                 # here laptop only will be used by the Students
     def __init__(self): 
        self.brand = 'HP'
        self.cpu = 'i5'
        self.ram = 8

     def show(self):
        print(self.brand,self.cpu,self.ram)   
                     
s1 = Students("Aryan",23)
s2 = Students("Saryan",22)

# print(s1.name, s1.rollno) #or

s1.show()

lap1 = s1.lap  
lap1 =Students.Laptop() 

# can create object of inner class outside the outer class provided you but 
# use outer class name to call it 


#---------------------------------------------------------------------------------------------------------------#
#                                       OOPS Concepts
#---------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------#
#                                       1. Inheritance : 
#---------------------------------------------------------------------------------------------------------------#

# It is a creating a new class which is the dreivative of the existing class
# Means from parent classa to sub or child class.
 
'''
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class

# Note:
python uses Method Resolution Order (MRO) that determines the flow of execution. 
MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, 
which refers to the order or sequence in which the interpreter will look for 
the variables and functions to implement. 
'''
class A:
   def __init__(self) -> None:
      print("it is init in A ")

   def func1(self):
      print("func1 is working in A")
   def func2(self):
      print("func 2 is working")

class B(A):  # B is ineriting feature of A means B is sub class and A is super or parent class

   def __init__(self) -> None:
    #  super().__init__() # It will access the all the features of the parent class , so init of A and init of B s called
      print("it is init of B")
   def func1(self):
      print("func1 is in B") # same method in A and B class so the method in the left will be priotize in the order
   def func3(self):
      print("func 3 is working")
   def func4(self):
      print("func 4 is working")

class C(B):  # C is ineriting feature of A, B so it is multilevel inherit.
   def func5(self):
      print("func 5 is working")

class D(A):  # D is ineriting feature of A
      def func6(self):
        print("func 6 is working")

class E(B,D): # Have to create this class for multilevel to avoid the MRO conflicts
   print(" Func 7 is working from class E as multilevel and avoid the MRO")
   def __init__(self) -> None: # 1st init of itself than the inti of the super is called
      super().__init__()
      # In the multilevel inherit the method is always preferd from the left to right like it will call from B first not D
   def feat(self):
      super.func1() # Method of super class


a1 =A()
b1= B()
c11= C()
d1 = D()
e1 =E()
a1=E()

a1.func1()
a1.func2() 
b1.func1() # inerited from A, Single level inheritance
b1.func3()     
c11.func1() 
c11.func5()
d1.func1()
e1.func4() # Multilevel inheritance

#---------------------------------------------------------------------------------------------------------------#
#             Constructor in inheritance : How constructor behave in inherit.
#---------------------------------------------------------------------------------------------------------------#
a1 =B() 
# the constructor is called for every function call in the class A
# When we don't have the init in the B then due to inheritance it will go to A if the relative method is called



#---------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------#
#                      2. Polymorphism :
#------------------------------------------------------------------------------------------------------------------#


#Ability of a function to change it's behaviour when it's called by differnet objects 
#example : built in "+" operator perform the additon for the integer data tuple and concation for the string data type 

#everything in Python is inherently an object, so when I talk about polymorphism, it can be an operator, method or any object of some class.
string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
# used the same operator () to perform on a string, integer and a list. You can see the () operator behaves differently in all three cases.

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

#The len() function is able to take variable inputs. In the example above it is a string and a list that provides the output in integer format.

#--------------------------------------------------------------------------------------------#
#                               3. Encapsulation: 
#--------------------------------------------------------------------------------------------#

# it limits the access to the method and varriables by encasing  them in a single unit of scope like class 
#it helps to prevent the unwanted modification and reduces the error occurence 


#********************************
#Encapsulation:
#*************************************

#  it have the method and varriables within the bounds of given unit like class , so member of class become locally bound to that class  
# it also used to hiding data and it's inrternal  represntation
#The use of single and double underscores for this hiding and represntation in Python is a substitute for this practice. 


class Alpha:

  def __init__(self):
    self._a = 2.  # Protected member ‘a’
    self.__b = 2.  # Private member ‘b’

 #self._a is a protected member and can be accessed by the class and its subclasses.
 # self.__b is a private member of the class Alpha and can only be accessed from within the class Alpha.

 # these private and protected members can still be accessed from outside of the class by using public methods to access them 
 # or by a practice known as name mangling, mangling is the use of two leading underscores and one trailing underscore, 
 #_class__identifier  # identifier is the data member that u want to access
#--------------------------------------------------------------------------------------------#
#_____________________
#                                    4. Abstraction : 
#__________________________
#--------------------------------------------------------------------------------------------#

# It hides the implementations details for the data security 
# python does not support the abstraction directly and uses the inheritance to achive it .
# it is used for hiding important get_schoolrmation as well as unnecessary get_schooliformation in a block of code. 

#the implementation of something called abstract classes and methods, 
# which can be implemented by inheriting from something called the abc module. "abc" here stands for abstract base class.
#It is first imported and then used as a parent class for some class that becomes an abstract class. 

from abc import ABC   
class ClassName(ABC):
    pass


#def __init__(self):  
 # __init_(self) : __init__ is the constructor for a class. The self parameter refers to the instance of the object
 #  class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
 #The __init__ method gets called after memory for the object is allocated:

   # x = Point(1,2)   #here self._x , self._y sets the member of the object Point .    


#-------------------------------------------------------------------
#                         running the methods 
#----------------------------------------------------------
print('{} {}'.format(emp1.first,emp1.last))
# or
print(emp1.fullname()) #emp1 instance is getting passed on 
print(emp2.fullname())

emp1.fullname() #calling the method, no need to pass on self

#class Method 
print(Employee.fullname(emp1)) #in this we have to manually pass on the instance emp1



#Expalantion to above method of code

  #Instance varriable contains data that is unique to each instances
emp1.first ='JP'
emp1.last = 'PAL'
emp1.email ='email.com'
emp1.pay = 600000

emp2.first ='JP'
emp2.last = 'PAL'
emp2.email ='email.com'
emp2.pay = 600000

print(emp1.email)
print(emp2.email)
