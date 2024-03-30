# Magic Methods and Implementing the operator overloading

#these special methods are always soruonded by the '__' or dunder
# Like __init__ , first or common special method
# Two other special methods are : __repr__, __str__


class Employee:  #class is the blueprint for creating the instances
   
   num_of_emolyee =0
   raise_amount = 1.04

   def __init__(self,first,last,pay):  
        self.first =first      
        self.last = last
        self.pay =pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emolyee += 1
   
   def fullname(self):
        return '{} {}'.format(self.first,self.last)

   def apply_raise(self): #creating the method for raise in salary
        self.pay = int(self.pay *1.04)

# Special Methods

#__repr__ is meant be for unamigious  (not open to more than one interpretation:) representation  
# of the object and should use dofr the debugging and logging         
   def __repr__(self) -> str:  # this should be as minimum
         pass

#__str__ is meant to be more readbale represntation of an object 
# and  used to display to end- user 
      
   def __str__(self) -> str:
        pass

emp1 = Employee('Karan','Aluja',90000)
emp2= Employee('Saran', 'Kaur', 90909)       

print(emp1)
repr(emp1)
str(emp1)
  