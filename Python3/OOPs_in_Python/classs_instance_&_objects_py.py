
#--------------------------------------------------------------------------------------------------------------------#         


# Attribute referred as a varriable that are declared  in class
# Behaviour is associateds with methods in a class 

#Everything  in py is a object and derived from the object class 

#class create the new type of object and from which you can create the instances 

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
