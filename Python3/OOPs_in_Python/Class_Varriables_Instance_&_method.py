#Create a class
#Instantiate a class with varriables and methods 
#Discover resuable code 

#_______________________________________________________________________________________________________________________________-
''' 
 Two type of class method in python 

1. New method : responsible for cretaing and returning the new empty object 
2. init Method : It is similar to known as the constructer in other 
programming langauges ,takes the object created
using the new methods , along with new arguments 
 

#from msilib.schema import SelfReg
#from typing import Self
 
class recpie():
     def __new__(cls) -> Self: 
 #CLS is not a keyword but it is a convention act as a palceholder for passing the class as its first arguments 
          pass

     def __init__(self) -> None:   # self keyword  is also the convetion that , it is instance we passing as argument
                                  #it has no function istself but serve as palceholder for self refernece by instance object 
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

#_____________________________________________________________________________________________________________________________________

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

#-------------------------------------------------------------------------------------
# REGULAR Methods: automatically takes its first argument as instance self
# Class Methods : in this it automatically takes class as a first argument (cls), by adding @classmethod as decoraotrs
# Static Method:

#---------------------------
# 1. Class Methods
#------------------------------------------------------------------------------
class Emp:
     num_of_emps =0
     raise_amount =1.04

     def __init__(self,first,last,pay):
          self.first =first
          self.last = last
          self.email = first + '.' + last + '@email.com'
          self.pay = pay

          Emp.num_of_emps +=1

     def fullname(self):
          return '{} {}.'.format(self.first, self.last)

     def apply_raise(self):
          self.pay = int(self.pay * self.raise_amount)

     @classmethod
     def set_raise_amt(cls,amount):  # here class is first argument instead of the instance var. self, and we can't use class as a variable name 
          cls.raise_amount =amount  #it will set the new amount of raise

#Using the Alternative constructer that aloows to passing the any employee string 
     @classmethod
     def from_String(cls,emp_str):
          first ,last,pay =emp_str.split('-')
          return  cls(first,last,pay) #this is creting the new employee



Emp.set_raise_amt(1.05)
#emp_1.set_raise_amt(1.05)

emp_1 =Emp('JP','Pal',909090)
emp_2 = Emp('NA','Last', 100000)

print(Emp.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# Use case of class Method  for parsing a string (refer @classmethod method)
#____________________________________________________________________________
emp_str_1 = 'Johan-Dew-80909'
emp_str_2 = 'Steve-Kam-99090'

#first ,last,pay =emp_str_1.split('-')
#new_emp1 = Emp(first,last,pay)

#Use of the alternative constructer method 

new_emp1=Emp.from_String(emp_str_1)
print(new_emp1.email)
print(new_emp1.pay)

#--------------------------------------------------------------
#Example: 
# class method with date time Module :
#----------------------------------------------------------

#################################################################################

#2. Static method of Class:
#------------------------------
# this class behave like a function , and this method doesn't operate on instance or class
# and don't pass anything as a argument like self or cls
#-------------------------

class holiday:
     @staticmethod
     def is_workday(day):#passing the work argument only
       if day.weekday() ==5 or day.weekday() ==6:
          return False
       return True
import datetime
my_date =datetime.date(2024,4,1)

print(holiday.is_workday(my_date))







