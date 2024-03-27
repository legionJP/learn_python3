'''' 
object(__builtins__)  #The base class of the class hierarchy.
# objects(built -in class)
#every class in py inherits from built in base class called objcts , which is found in built-ins dot objects

#like
class Aclass()
    #means
class Aclass(object)    

class types:
1. Base class/parent/super

2. child/sub/derived class

# Child class extend the behaviour  and attributes of the parents class which allows to
1. Add more properties to child class

2. Modify inherited properties in child class

'''

class employee():
    def __init__(self,name,last) -> None:
        self.name=name 
        self.last =last 
class manager(employee):
    def __init__(self, name, last,position) -> None:
        super().__init__(name, last)
        self.position=position

class supervisors(employee):
    def __init__(self, name, last) -> None:
        super().__init__(name, last)
    def leave_request(self,days):
        return "You can take leave for " + str(days) +" days"   

#creating the instances for the classes 

puneetS=manager("Puneet","S","manager")

Jatav=supervisors("AJ","J")
Satav=supervisors("SS","s")

print(Jatav.leave_request(4))
print(puneetS.position)
print(Satav.name)


#Multiple Inheritance 

#Single Inheritence 

class A():
    pass
class B(A):
    pass


#Multiple Inheritence 

class A():
   a = 1
   
class B():
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# two classes called A and B are created and then variables a and b respectively are initialized with values. 
#  A new class C is then defined and classes A and B are passed to it. 
#  This is how multiple inheritance is done in Python.

# Multi Level Inheritance

class A():
    a=1
class B(A):
    b=2
class C(B):
    pass
c = C()
print(c.a)    
print(isinstance(c,A))

#there are three level of inheritance 
# Above example of multi-level inheritance where the derived class C inherits from base class B.
 #The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. 


#Built in Functions 

#There are two built-in functions that can come in handy when trying to find 
#  the relationship between different classes and objects: issubclass() and isinstance().

issubclass(A,B)
print(issubclass(A,B)) # is A  subclass of B 
print(issubclass(C,A)) # is C subclass of A 
 

 #Super() function.

 #The super() function is a built-in function that can be called inside the derived class and gives access to the methods and 
#variables of the parent classes or sibling classes.
 

class Fruit():
    def __init__(self,fruit) -> None:
        print('Fruit type', fruit)

class FruitFlavour(Fruit):
    def __init__(self) -> None:
        super().__init__('apple') # changes inside the derived class
        print("Appple is sweet")

apple=FruitFlavour()
 
#This happened because when you initialize the child class, you don’t initialize the base class with it. 
#  super() function helps you to achieve this and add the initialization of base class with the derived class.




