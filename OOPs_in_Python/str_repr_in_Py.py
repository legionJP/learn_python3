
# difference between str() and repr()
a = [1,2,3,4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

# class str(object = '') the goal of the str is readable

# repr(object) , the goal of the repr is anambigious 

import datetime
import pytz

at= datetime.datetime.now(datetime).replace(tzinfo=.UTC)
b = str(a)

print('str(a){}'.format(str(a)))
print('str(b){}'.format(str(b)))

print

print('repr(a):{}'.format(repr(a)))

print('repr(b):{}'.format(repr(b)))

print