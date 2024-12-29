#------------------------------------------------------------------------------------------------------------------#
#                               Iter, Iterator and Iterables : 
#------------------------------------------------------------------------------------------------------------------#

# Iterables : this is something which can be looped over so  list is the iterables 

'''Specificly 
it means that object needs to return an iterator object from its __iter__ method 
and iterator that is returend from __iter__ methos must define __next__ method which 
accesses elements container one at a times '''

#1. Iterable: An object you can iterate over (e.g., lists, strings).

#2. Iterator: An object that provides a stream of data and has __iter__() and __next__() methods.

#3. iter(): A function to obtain an iterator from an iterable.


''''

iter(): A built-in function to obtain an iterator from an iterable.

__iter__(): A special method in an iterable object that returns an iterator.

next(): A built-in function to get the next item from an iterator.

__next__(): A special method in an iterator that returns the next item.
'''

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[2])

for num in nums:
    print(num)

print(dir(nums)) 

# if something is iterable than it must have the method called -__iter__()


# so for loop is calling the method __iter__ on the object and retruning the iterator 

#Iterator: so iterator is a object in a state and it remeber where it is during iterations 
#and they get their next value by the __next__ method

#print(next(nums))
#list doesn't have the __next__ method so it isn't  iterator 

#-----------------------------------------------------------------------------------#-----------------------------------
#                         Implement the iter method on the list 
#------------------------------------------------------------------------------------------------------------------#

#object is the iterator in a state so it rember where it is during the iterations 

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))

#------------------------------------------------------------------------------------------------------------------#

i_nums = nums.__iter__()
#i_nums= iter(nums)
print(i_nums)
print(dir(i_nums))
print(next(i_nums))
print(next(i_nums)) 
print(next(i_nums))
print(next(i_nums))
#print(next(i_nums)) #stop iteration error 


# so working of the for loop as a iterator follows :
'''
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
'''

#------------------------------------------------------------------------------------------------------------------#
    # Creating the Own iter method
#------------------------------------------------------------------------------------------------------------------#

#1.
class Top10:
    def __init__(self) -> None:
        self.num =1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=10:                
            val = self.num
            self.num+=1
            return val
        
        else:
            raise StopIteration
        
values = Top10()

print(next(values)) # after this only print the from value2
for i in values:
    print("Value",i)


#--------------------------------------------------------#--------------------------------------------------------#
#      2.                                    Own Range Function
#--------------------------------------------------------#--------------------------------------------------------#
# It is  function for behaving like the built-in class of range function 

class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end 
        
    def __iter__(self):   #making the class iterable 
        return self      
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1 
        return current
    
#--------------------------------------------------------#--------------------------------------------------------#


    
