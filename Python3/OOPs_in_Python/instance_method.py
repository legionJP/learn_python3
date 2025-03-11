class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name= name 
        self.payment= payment  #self.varriable =varriable or attribute
        self.amount=amount
    def pay(self):
        self.payment ="yes"

    def status(self):
        if self.payment=="yes":
            return self.name +" is paid "+ str(self.amount)
        else:
            return self.name + "is not paid yet"
                
#creating the instance of the class

nathan =Payslips("nathan","no",10000)
jp= Payslips("JP","yes",2000)
print(nathan.status(),"\n",jp.status())   #calling the fun with the instances
nathan.pay()  #pay fun is made for the updating the value of the payment so,
print(nathan.status(),"\n",jp.status())  # status is the  Method
print(jp.payment)
print(nathan.payment)

#Here the value of the pay is changed for the nathan not for jp , this is because 
#Method inside the class is not affected by changing the one instance.

 
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