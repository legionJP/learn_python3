#Python Logging Advanced - Loggers , Hamdlers , and formatters

'''
DEBUG:root:Add: 10 + 5= 15
WARNING:root:Add: 10 + 5= 15
DEBUG:root:Subtracr: 10 - 5= 5
DEBUG:root:Multiply: 10 * 5= 50

#here root is the dafault logger configuration
'''


import logging  #buit-in module
from  employee_log import Employee

#creating the logger variable
logger =logging.getLogger(__name__) #for convettion __name__ =__main__ method , when the code is executed by import it name will be equal to module name

'''
after assigning the var we have to use the logger.info , instead of logging.info.

-> these logger are in hirerarchy if employee logger doesn't have something set than it will
fallback to root logger

'''

logging.basicConfig(filename='sample.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s') #DEBUG is the constant but int in the back ground

#here format for time from documentation is %(asctime)s:, and for levelname is %(levelname)s, for message it is %(message)s

#-----------------
#NOTE: the sample.log file is not created because when we are importing employee so the employee.log is also 
#sharing same root logger than its only log employee.log. 
#if we change the log level to '.info' than it will log add, subtract ,.. but in one file
#-------------

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
 
logger.info('Add: {} + {}= {}'.format(num1,num2,add_result)) #its not logging the debug  when the logging config level was not declared 
logger.info('Add: {} + {}= {}'.format(num1,num2,add_result))

sub_result = subtract(num1,num2)
#print('Subtracr: {} - {}= {}'.format(num1,num2,sub_result))
logger.info('Subtracr: {} - {}= {}'.format(num1,num2,sub_result))

multi_result = multiply(num1,num2)
# print('Multiply: {} * {}= {}'.format(num1,num2,multi_result))
logger.debug('Multiply: {} * {}= {}'.format(num1,num2,multi_result))

div_result = divide(num1,num2)
#print('divide: {} / {}= {}'.format(num1,num2,div_result))
logger.debug('divide: {} / {}= {}'.format(num1,num2,div_result))
#logging.debug('divide: {} / {}= {}'.format(num1,num2,div_result))

