import logging
logging.basicConfig(filename='employee.log',level=logging.INFO,
                    format='%(levelname)s:%(message)s')

class Employee:   
   
   def __init__(self,first,last):  
        self.first =first      
        self.last = last
        
        logging.info('Created Employe {}- {}'.format(self.fullname, self.email))

   @property    
   def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
   @property
   def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

emp1 = Employee('jp','pal')
emp2 =Employee('ak','kat')
emp3 =Employee('sk','nat')