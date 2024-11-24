
#Property Decorators - Getters , Setters , Deleters : 

class Employee:  #class is the blueprint for creating the instances
   
   num_of_emolyee =0
   raise_amount = 1.04

   def __init__(self,first,last):  # METHOD 1
        self.first =first      
        self.last = last
        #self.pay =pay
        #self.email = first + '.' + last + '@email.com'

        Employee.num_of_emolyee += 1

   @property
   def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
   @property
   def email(self):
       return '{}.{}@email.com'.format(self.first,self.last) 
   
   #setting the full name by the setter for 
   # emp1.fullname = 'JP PAL'

   @fullname.setter
   def fullname( self, name):
       first , last = name.split(' ')
       self.first = first
       self.last = last

   @fullname.deleter
   def fullname(self):
       print('Delete Name!')
       self.first = None
       self.last = None

emp1 = Employee('JP', 'PAL') 

emp1.fullname = 'JP PAL' #changing the fullname 

emp1.first = 'Jay' # here first name is changed but the eamil is same , so fixing this issue by property decorators 

print(emp1.first)
print(emp1.last)
print(emp1.email)
#print(emp1.fullname()) , run this if not using @property decorator 
print(emp1.fullname)  #defining it as a method but accessing as a attribute

del emp1.fullname # () not used bcz accesing as a attribute
print(emp1.fullname)


'''
Note, Normally Python doesn't allow you to have multiple methods with the same name
and different number of parameters. However,
 in this case Python allows this because of the decorators used.

'''

