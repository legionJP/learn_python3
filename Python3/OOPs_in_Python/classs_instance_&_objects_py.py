
#--------------------------------------------------------------------------------------------------------------------#         


# Attribute referred as a varriable that are declared  in class
# Behaviour is associateds with methods in a class 

#Everything  in py is a object and derived from the object class 

#class create the new type of object and from which you can create the instances 
'''
Object:

An object is a fundamental concept in OOP. 
It represents a concrete entity that combines data (attributes) and behavior (methods).

The term "instance" emphasizes the relationship between an object and its class.
 When we create an object from a class, we say that we "instantiate" the class.
'''


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"This car is a {self.make} {self.model}")

#let's create an object of this class:      
my_car = Car("Toyota", "Corolla")
my_car.display()  # Output: This car is a Toyota Corolla

'''Car is the class.

my_car is an object of the class Car.

my_car is also an instance of the class Car.
'''
#--------------------------------------------------------------------------------------------------------------------#
#2.

class Myclass:
    #pass    
    # pass plays the role of the placeholder when nothing needs to be excecuted 
    
    print("hello class") 
    a =10          
    def hello_method(self): 
        print("hello Method  defined ")


    def hello_method1(self,num_method): 
        total_method= num_method*self.a   
        return total_method  
    
#--------------------------------------------------------------------------------------------------------------------#         
#Creating the method inside the class ,  
# self is an instance method and facilitates the method to point to any instance of the hello_method()
# It should be noted  that any number of parameters can be passed to these instance methods but
# the first one is always the reference to the instance of that class.
#--------------------------------------------------------------------------------------------------------------------#
         
obj_myclass =Myclass()
#Creating the object of the class  for declaring the instances 
#created the object by assigning the  varriable and showing the instansation reference
print(obj_myclass)
print(Myclass.a) 
# attribute reference to class 
print(obj_myclass.a) 
# instance refernece to a class 
print(obj_myclass.hello_method())
print(obj_myclass.hello_method1(3))

#--------------------------------------------------------------------------------------------------------------------#
#                                  Class and Object Excercise and demostrations : 
#--------------------------------------------------------------------------------------------------------------------#


class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
#print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")

class MyClass:
    def my_method(this,var):
        print("Hello, this is MyClass!")
        print(this)
        this.var=var
        print(var)
        
obj = MyClass()
obj.my_method(9)

class Example:
    def __init__(self, value):
        self.value = value  # self.value is an instance variable

    def display_value(self):
        print(self.value)  # Accessing the instance variable

# Creating an instance
obj = Example(42)
obj.display_value()  # Output: 42

#--------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------------------#         
#                                               Type of the object :
#--------------------------------------------------------------------------------------------------------------------#

'''
class object 
instance object 
and 
Mehtod object                    
              
here Myclass is   the class object and the 
obj_myclass is the instance of the myclass
'''
#Note: Classes perform to types of operation  1. attribute refrences   2. isinstansiating
 
#Instansitaion process in python involves three key procees 
# 1. Class Defination
#2. Creating the new instance 
#3.  Intitalizing the new instance 

#1.  Instance Objects:
# These are the most common type of objects and represent individual instances of a class.
#  Each instance object has its own set of instance variables.

#--------------------------------------------------------------------------------------------------------------------#

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# 2. Class Objects:
# The class itself is also an object.
#  It is an instance of the type metaclass in Python and defines the blueprint for creating instance objects.

# Class variables (attributes) are shared across all instances of the class.


class Car:
    number_of_wheels = 4  # Class variable

    def __init__(self, make, model):
        self.make = make
        self.model = model

print(Car.number_of_wheels)  # Accessing class variable

# 3. Static Method Objects:
# These methods belong to the class rather than any instance. 
# They don't require access to the instance (self) or the class (cls).

class Car:
    @staticmethod
    def is_motor_vehicle():
        return True

print(Car.is_motor_vehicle())  # Output: True

# 4. Class Method Objects:
# These methods have access to the class itself via the cls parameter and can modify class state.


class Car:
    number_of_wheels = 4

    @classmethod
    def set_number_of_wheels(cls, num):
        cls.number_of_wheels = num

Car.set_number_of_wheels(6)
print(Car.number_of_wheels)  # Output: 6

# 5. Inner Class Objects:

# A class defined within another class. 
# Inner classes can help logically group classes that are only used in one place.


class OuterClass:
    class InnerClass:
        def __init__(self, value):
            self.value = value

outer_instance = OuterClass()
inner_instance = OuterClass.InnerClass(42)
print(inner_instance.value)  # Output: 42

'''Summary:
In a class, you will typically deal with:

Instance Objects for creating specific instances of the class.

Class Objects for defining shared attributes and methods.

Static and Class Method Objects for methods associated with the class itself.

Inner Class Objects for nested class definitions.'''

#--------------------------------------------------------------------------------------------------------------------#