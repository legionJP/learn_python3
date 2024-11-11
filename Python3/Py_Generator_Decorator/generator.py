# Function for  square Number

def square_number(num):
    result =[]
    for i in num:
        result.append(i*i)
    return result 

my_num = square_number([11,22,33,44,55,66,77,88,99]) 
#my_num = [x*x for x in [1,2,3,4,5,6,7,8,9]] # list comprehension
 
#--------------------------------------------------------------------------------

#my_num = (x*x for x in [1,2,3,4,5]) # generator expression
#print(list(my_num)) #coverting into list item

print(my_num)

#----------------------------------------------------------------------------------------------------

# Converting into generator (getting square by the help of generator ) 

def square_num(nums):
    for i in nums:
        yield i*i

my_nums = square_num([11,22,33,44,55,66])
print(my_nums)

# printing the generater object address bcz  it does not hold the value in memory
# it yield the value one by one in every iteration
'''
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
'''
# using the loop
for square in my_nums:
    print(square)

#------------------------------------------------------------------------------------------------
    
#Example of generator use

import mem_profile
import random 
import time 

names = ['John', 'Carry', 'Adam', 'Gill' ,'Rohit', 'Ashwin']
majors = ['math','WK' , 'CompSci', 'Batting', 'Pullshot', 'Carromball']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = { 
                    'id': 1, 
                    'name': random.choice(names),
                    'majors': random.choices(majors)
             
                  }
        result.append(person)
    return result

def people_generaotr(num_people):
    for i in range(num_people):
        person ={
                  'id': 1,
                  'name': random.choice(names),
                  'majors': random.choices(majors)

        }         
        yield person

'''
t1 = time.process_time()
people = people_list(1000000)
t2 = time.process_time()

print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} Seconds'.format(t2-t)
'''
t1 = time.process_time()
people = people_generaotr(1000000)
#people = list(people_generaotr(1000000))

t2 = time.process_time()

print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} Seconds'.format(t2-t1))  # it didnt take any extra memory

#-------------------------------------------------------------------------
