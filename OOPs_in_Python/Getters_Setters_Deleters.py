
#Property Decorators - Getters , Setters , Deleters : 

class Employee:  #class is the blueprint for creating the instances
   
   num_of_emolyee =0
   raise_amount = 1.04

   def __init__(self,first,last):  # METHOD 1
        self.first =first      
        self.last = last
        #self.pay =pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emolyee += 1
   
   def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = Employee('JP', 'PAL') 

emp1.first = 'Jay' # this is 

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname())






