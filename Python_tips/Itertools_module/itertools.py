# ==========================================  Iterators functions for Efficent looping #====================

import itertools
counter1 = itertools.count() #it will work for any size of the data 

#for num in counter:
    #print(num)

#-------------------------------------------
# Using of the count() function for the iterations 
#-------------------------------------------

counter = itertools.count(start=5, step=5)
#counter = itertools.count(start=5, step=2-.5)

print(next(counter))
print(next(counter))
print(next(counter))


# Example of list data using the itertools modules:
#---------------------------------
# using of the zip function
#--------------------------------
data = [100,200,300,400]

data_index_count = list(zip(itertools.count(), data)) #zip combine the two iterables 
print(data_index_count)


#----------------------------------------------------------
# Use of zip_logest and range() function in iter or itertools
#-------------------------------------------------------

data1 = [100,200,300,400]
data_index_count1 = list(itertools.zip_longest(range(10),data1))
print(data_index_count1)

#-------------------------
# Use of the cycle() function
#--------------------------

c_counter = itertools.cycle([1,2,3,4])  #Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.
String_cycle = itertools.cycle(('On','Off'))
print(next(String_cycle))
print(next(String_cycle))
print(next(String_cycle))
print(next(String_cycle))
print(next(c_counter))
print(next(c_counter))
print(next(c_counter))
print(next(c_counter))
print(next(c_counter))
print(next(c_counter))
print(next(c_counter))


#-------------------------
# Use of repeat
#--------------------------
r_counter = itertools.repeat(2,times=4)
print(next(r_counter))
print(next(r_counter))
print(next(r_counter))
print(next(r_counter))
#print(next(r_counter))  #stop iteration errror 

#use of map in the repeat fun 
squares = map(pow,range(10), itertools.repeat(2))
print(list(squares))

#-----------------
# use of starmap 
#----------------
squares = itertools.starmap(pow,[(0,2),(1,2),(2,2)])  # it will return the base 2 , power 0  using theargument tuple taken from the given sequence.
print(list(squares))

#-------------------------
#Use of the Combinations and permutations : 
#-------------------------

letters =['a','b','c','d']
numbers = [1,1,2,3,4,0,4,5]
names = ['JPPAL', 'Sachin']

result  =  itertools.combinations(letters,2) 
#result  =  itertools.permutations(letters,2)  #for reverse combinations use permutations

for item in result:
    print(item)

cr_result = itertools.combinations_with_replacement(numbers,4)    #for succesive repetations 
print(list(cr_result))
#-----------------------------------------------------------------------------
#Use of the product  class for the repeated combinations or permutaions of numbers:

n_result = itertools.product(numbers,repeat=4)
print(list(n_result))

# Using of the chain()

#without chain 
combined = itertools.chain(letters,numbers,names)
for item in combined:
    print(item)

#performing the slice on the iterator islice()    

result_slice = itertools.islice(range(10),6)  #. Works like a slice() on a list but returns an iterator.
result_slice2 = itertools.islice(range(10),1,6,2) #start  ,end and step  point 
for item in result_slice2:
    print(item)
print(list(result_slice))

#-------------------------------------------------------
# islice() on the file for slicing particular part of file 
#--------------------------------------------------------

with open ('test.log','r') as f:
    header = itertools.islice(f,3) #will print the first three line of file

    for line in header:
        print(line , end="")


# Use of the compress fintion :

selectors = [True, False, False, True]

s_results = itertools.compress(letters, selectors) #in this value are passed as iterable 

for item in s_results:
    print(item)

#--------------------
# filter function use 
#----------------------
def list_f(n):
    if n>2 :
        return True
    return False
#f_result = filter(list_f, numbers) 

# filterflase() function usse in itertools :

f_result = itertools.filterfalse(list_f, numbers) 
for item in f_result :
    print(item)

# Use of the dropwhile() and takewhile()

#d_result = itertools.dropwhile(list_f,numbers)
d_result = itertools.takewhile(list_f,numbers)

for item in d_result:
    print(item)

import operator                                        
#  use of accumulate() function  

a_result = itertools.accumulate(numbers) # add the value in series 
for item in a_result:
    print(item) 
    
# use of the operator.mul() for multiplication of data
mul_result = itertools.accumulate(numbers, operator.mul)
#numbers = [1,1,2,3,4,1,4,5]
for item in mul_result:
    print(item)

#-----------------------------------------------------
# Grouping the dict list on the basis of key group :
#------------------------------------------------------

import itertools

def get_state(person):   #list inside the dict 'people'
    return person['state'] #group by the state 

People = [
    {
        'name': 'Johan',
        'city': 'New York',
        'state' : 'NY'
    },
    {
        'name': 'Risabh',
        'city' : 'Delhi',
        'state': 'NCT Delhi'

    },
    {
        'name': 'Surya',
        'city': 'Mumbai',
        'state': 'MH'
    },
    {
        'name': 'Rohit',
        'city': 'Mumbai',
        'state': 'MH'

    },
     {
        'name': 'Axar',
        'city': 'Varoda',
        'state': 'Gujrat'
        
    }
]

person_group = itertools.groupby(People,get_state) #get_state is key, each item will be the tuple of key as state and the iterable of the all item in group

for key , group in person_group:
    #print(key, group)
    print(key)
    for person in group:
        print(person)
    print()    
    
    #know the number of person in the group 
    print(key,len(list(group)))

#using the own type of the iterators in place of the person_group

iter1, iter2 = itertools.tee(person_group)
 