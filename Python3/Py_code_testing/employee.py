import requests
from unittest.mock import patch  #we can use patch as a decorater or as a context manager 

# Patch wil allow us to mock  a object during a test and then the 
#object is atumatically restored after the test is run 

class Employee:   
   raise_amount = 1.05
   def __init__(self,first,last,pay):  
        self.first =first      
        self.last = last
        self.pay = pay
        
        
   @property    
   def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
   @property
   def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
   
   def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Mocking Method : 
# you want to get some info from web but website is down so your function will fail, so to avoid this 

def monthly_schedule(self, month):
     response = requests.get(f'http://company.comm/{self.last}/{month}')
     if response.ok:
          return response.text
     else:
          return 'Bad Requests'