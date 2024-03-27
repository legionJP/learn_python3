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
