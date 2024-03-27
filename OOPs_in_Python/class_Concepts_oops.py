#Programming paradigm are the strtagey for reducing the code complexity and determine the flow of the code 

'''type of the paradigm like 

1. Declarative , Procedural , Object oriented , function , Logic  object , Event driven , flow driven 

In pyhton Paradigm follows , Object Oriented , Procedural and functional


#Object Oriented Programming 

oop is 
Resuable , Abstracrtion , Move between projects 


#Key Components of the OOPS 

1. Classes  :

Class is a logical code blocks , it contains : 

                Attributes : these can be a varriable
                Behaviour : behiour can be a function 

 We can create the instances of the classes called the object or class provide a blueprint for creating a object. 

2. Object :  
An attributes and Behaviour of the class define the state of the Object :
 example : Creating the object emp1 
 by calling the class employee()
       

class employee(position, emp_status):
    def postion():         
        return  "I am a (postion,emp_status)"
    
#Object Creating OR Creating the instances of the class 
emp1 = employee("shift_lead", "ft")  

3. Methods :  (It is function that is associate with class )
methods are the functions that are defined inside the class and determine the behviour of the object instances 

emp1.postion()   #method 

'''

#OOPS Concepts

#1. Inheritenace : 

# It is a creating a new class which is the dreivative of the existing class means from parent classa to sub or child class.

'''
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class

python uses Method Resolution Order (MRO) that determines the flow of execution. 
MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, 
which refers to the order or sequence in which the interpreter will look for the variables and functions to implement. 

'''

#__________________________
#2. Polymorphism :
#__________________________

#Ability of a function to change it's behaviour when it's called by differnet objects 
#example : built in "+" operator perform the additon for the integer data tupe and concation for the string data type 

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




#3. Encapsulation: 

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

#_____________________

#4. Abstraction : 
#__________________________

# It hides the implementations details for the data security 
# python does not support the abstraction directly and uses the inheritance to achive it .
# it is used for hiding important information as well as unnecessary information in a block of code. 

#the implementation of something called abstract classes and methods, 
# which can be implemented by inheriting from something called the abc module. "abc" here stands for abstract base class.
#It is first imported and then used as a parent class for some class that becomes an abstract class. 

from abc import ABC   
class ClassName(ABC):
    pass


#def __init__(self): 
''' 
 # __init_(self) : __init__ is the constructor for a class. The self parameter refers to the instance of the object
 #  class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
 #The __init__ method gets called after memory for the object is allocated:

   # x = Point(1,2)   #here self._x , self._y sets the member of the object Point .    

'''


#-------------------------------------------

#Instances of the classes
#--------------------------------------
class Employee:  #class is the blueprint for creating the instances
   
   def __init__(self,first,last,pay): #first instance is self
        self.first =first                                  # this method called intialize and in other language  it called as constructer
        self.last = last
        self.epay =pay
        self.email = first + '.' + last + '@email.com'


emp1= Employee('jp','pal',50000)
emp2 = Employee('name1','last',20000)
# print(emp1)
# print(emp2)
print(emp1.email)
print(emp2.email)



'''

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

'''