#-------------------
#Iter and Iterables : 
#-------------------
#Iterables : this is something which can be looped over so  list is the iterables 

#Specificly it means that object needs to return an iterator object from its __iter__ method 
# and iterator that is returend from __iter__ methos must define __next__ method which 
# accesses elements container one at a times 

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

#-----------------------------------
#Implement the iter method on the list 
#-----------------------------------

#object is the iterator in a state so it rember where it is during the iterations 


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



#--------------------------------------------------------
# function for behaving like the builtin class of range function 
#--------------------------------------------------------
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

#Creating generator function iterator  : 

def myrange(start , end):  
    current = start
    while current < end : # While   True: 
        yield current
        current += 1 

#------------------------------------------
# use of generator fun and Range Class : 
#------------------------------------------
nums = myrange(1,10)

# nums = MyRange(1,10)

#Looping the gen fun or class
for  num in nums :
    print(num)

#or by next() method     
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))



#-----------------------------
# Coding Problem : Creating own Iterators :
#----------------------------

class Sentence:
    def __init__(self,sentence):
        self.sentence  = sentence
        self.index = 0 # adding the index attribute 
        self.words = self.sentence.split()

    #making class iterabale 

    def __iter__(self):
        return self 

    def __next__(self): # for the iterating the object at a iteration state 
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index 
        self.index += 1 
        return self.words[index] #returns the words index by index 

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)


# By using the Generator : 

def sentence(sentence):
    for word in sentence.split():
        yield word  #it will yield one by like the  __next __

my_sentence1 = sentence('This is a test')

for word in my_sentence1:
    print(word)
