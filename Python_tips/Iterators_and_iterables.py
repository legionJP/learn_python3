
#Iterables : this is something which can be looped over so  list is the iterables 

nums = [1,2,3,4]
for num in nums:
    print(num)

# if somwthing is iterable than it must have the method called -__iter__()

print(dir(nums)) 
# so for loop is calling the method __iter__ on the object and retruning the iterator 

#Iterator: so iterator is a object in a state and it remeber where it is during iterations 
#and they get their next value by the __next__ method

#print(next(nums))
#list doesn't have the __next__ method so it isn't  iterator 

#Implement the iter method on the list 

i_nums = nums.__iter__()
#i_nums= iter(nums)
print(i_nums)
print(dir(i_nums))

print(next(i_nums)) #object is the iterator in a state so it rember where it is during the iterations 
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums)) #stop iteration error 

# so working of the for loop as a iterator follows :
'''
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
'''

# function for behaving like the builtin class

class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end 
        
    def __iter__(self):
        return self      
    
    def __next__(self):
        