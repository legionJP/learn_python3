#Create a class
#Instantiate a class with varriables and methods 
#Discover resuable code 

#_______________________________________________________________________________________________________________________________-
''' 
 Two type of class method in python 

1. New method : responsible for cretaing and returning the new empty object 
2. init Method : It is similar to known as the constructer in other programming langauges , takes the object created
using the new methods , along with new arguments 
 

#from msilib.schema import SelfReg
#from typing import Self
 
class recpie():
     def __new__(cls) -> Self:   #CLS is not a keyword but it is a convention act as a palceholder for passing the class as its first arguments 
          pass

     def __init__(self) -> None:   # self keyword  is also the convetion that , 
                                  #it has no function istself but server as palceholder for self refernece by instance object 
          pass
     
#class recpie():
 #    def __new__(cls:type[SelfReg]) -> Self:
  #       pass  
        
''' 
#Class setup for the recpie class  

class Recpie():
    def __init__(self,dish,items,time) -> None:
          self.dish =dish
          self.items = items
          self.time = time
    def contents(self):
          print('the dish ' + self.dish + " has " +str(self.items)+ " and takes time " +str(self.time)+ " minutes to prepare")
          

#use some  instances by referencing the class 

Pizza=Recpie("cheese_pizza ",["chees","totmato","sauce"],"15")
Poha= Recpie("Poha",["peanut","totmato","sauce"],"25")

print(Pizza.items)
print(Poha.items)

#Print the instance method  Contents over object Pizaa or poha 

print(Pizza.contents())


#_------------------------------------------------------------------------------
# 2. Class Varriables
#------------------------------------------------------------------------------

#Instance varriable should be unique for each instance 
#But class varriables are same for each instance

class Employee:  #class is the blueprint for creating the instances
   
   num_of_emolyee =0
   raise_amount = 1.04
   def __init__(self,first,last,pay): #first instance is self
        self.first =first      # this method called intialize and in other language  it called as constructer
        self.last = last
        self.pay =pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emolyee += 1
   
   def fullname(self):
        return '{} {}'.format(self.first,self.last)

   def apply_raise(self): #creating the method for raise in salary
        #self.pay = int(self.pay *1.04) #??? 1....
        #Acessing the class var need to access trhough class or from instance of class
        #self.pay = int(self.pay *Employee.raise_amount) #Accessing  var. through class
        self.pay = int(self.pay *self.raise_amount) #access trhough instance, this allows to changes the amt for single instance

emp1 = Employee('JP', 'Pal',45000)
emp2 = Employee('AK','asd', 56432)  

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

#Employee.raise_amount =1.05 #change for emp1 
emp1.raise_amount =1.05 # changes in whole instances

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emolyee)

#Printing the namespace of the instnace emp1
print(emp1.__dict__)
print(Employee.__dict__) #class contian the raise_amount attribute so the instance access this from class
















