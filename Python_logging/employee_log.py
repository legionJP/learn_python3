import logging
import logging.handlers

#adding the fromat to handler 
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#creating the logger variable
 #for convettion __name__ =__main__ method , when the code is executed by import it name will be equal to module name
 
logger =logging.getLogger(__name__)  

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logging.basicConfig(filename='employee.log',level=logging.INFO,
                    format='%(levelname)s:%(message)s')     

class Employee:   
   
   def __init__(self,first,last):  
        self.first =first      
        self.last = last
        
        logger.info('Created Employe {}- {}'.format(self.fullname, self.email))

   @property    
   def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
   @property
   def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

emp1 = Employee('jp','pal')
emp2 =Employee('ak','kat')
emp3 =Employee('sk','nat')