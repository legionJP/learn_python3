
# difference between str() and repr()
a1 = [1,2,3,4]
b1 = 'sample string'

print(str(a1))
print(repr(a1))

print(str(b1))
print(repr(b1))

#-------------------------------------------------------------------------------------------------
# class str(object = '') the goal of the str is readable

# repr(object) , the goal of the repr is anambigious 

import datetime
import pytz

timezone = pytz.timezone('Asia/Kolkata')

a= datetime.datetime.now(timezone)
b = str(a)

print('str(a){}'.format(str(a)))  #this is more readable 
print('str(b){}'.format(str(b)))

print()

print('repr(a):{}'.format(repr(a)))  # this is unambigious , usefull for the developers, if it is string or

print('repr(b):{}'.format(repr(b)))

print()