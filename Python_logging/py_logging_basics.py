#logging Basics : Logging to files , Setting levels and Formatting

#Logging Levels : There are 5 logging levels : debug , info , warning, eroor and critical 

#1. Debug : Detailed information typically of interset when diagnosing the problems.

#2. Info : Confirmations that things are working as expected

#3. Warning : An indecation that something unexpected happen , or indicate some problem in near 
#future eg. 'disk space is low':  

#4. Error : due to some serious problem , the software has not been able to perform some function

#5. Critical : A serious error , indicate that program itself may be  unable to  running 

# as a defualt it will log warning , Errror , critical and ingore debug , info 


'''
import logging  #buit-in module

logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s') #DEBUG is the constant but int in the back ground

#here format for time from documentation is %(asctime)s:, and for levelname is %(levelname)s, for message it is %(message)s

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
num1 = 12
num2 = 11
add_result = add(num1,num2)
print('Add: {} + {}= {}'.format(num1,num2,add_result))
logging.debug('Add: {} + {}= {}'.format(num1,num2,add_result)) #its not logging the debug  when the logging config level was not declared 
logging.warning('Add: {} + {}= {}'.format(num1,num2,add_result))

sub_result = subtract(num1,num2)
#print('Subtracr: {} - {}= {}'.format(num1,num2,sub_result))
logging.debug('Subtracr: {} - {}= {}'.format(num1,num2,sub_result))

multi_result = multiply(num1,num2)
# print('Multiply: {} * {}= {}'.format(num1,num2,multi_result))
logging.debug('Multiply: {} * {}= {}'.format(num1,num2,multi_result))

div_result = divide(num1,num2)
#print('divide: {} / {}= {}'.format(num1,num2,div_result))
logging.debug('divide: {} / {}= {}'.format(num1,num2,div_result))

'''
#-------------
#Example 2:
#-------------
import logging

logging.basicConfig(filename='employee.log',level=logging.INFO,
                    format='%(levelname)s:%(message)s')
class Employee:  #class is the blueprint for creating the instances
   
   def __init__(self,first,last): #first instance is self
        self.first =first      # this method called intialize and in other language  it called as constructer
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

 