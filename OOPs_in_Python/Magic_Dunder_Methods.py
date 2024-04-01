# Magic Methods and Implementing the operator overloading

#these special methods are always soruonded by the '__' or dunder
# Like __init__ , first or common special method
# Two other special methods are : __repr__, __str__


class Employee:  #class is the blueprint for creating the instances
   
   num_of_emolyee =0
   raise_amount = 1.04

   def __init__(self,first,last,pay):  # METHOD 1
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
# of the object and should use for the debugging and logging   

 #Method 1              
   def __repr__(self) -> str:  # this should be as minimum
         return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)

#__str__ is meant to be more readbale represntation of an object 
# and  used to display to end- user 
      
   def __str__(self) -> str:  # METHOD 3 
     return '{} -{}'.format(self.fullname ,self.email)
   
   # for combining the pay of the employee
   def __add__(self,other):
       return self.pay +other.pay
   
   # Function to check the length of the string like __len__ function
   def __len__(self):
       return len(self.fullname())
   

emp1 = Employee('Karan','Aluja',90000)
emp2= Employee('Saran', 'Kaur', 90909)  

print(emp1 + emp2)
print(len(emp1))

print(emp1) #this will print the employee object as a string

print(repr(emp1))
print(str(emp1))

#or

print(emp1.__repr__())  
print(emp1.__str__())  

# these two methods are same allows us to change how our object will display 
#--------------------------------------------------------------------------------

# Specials Methods for Airthmetics

print(1+2) #this method uses __add__ method

print(int.__add__(1,2))

#string dundder method
print(str.__add__('a','b'))


# Function to check the length of the string 

print(len('Simple'))
#or
print('test'.__len__())
