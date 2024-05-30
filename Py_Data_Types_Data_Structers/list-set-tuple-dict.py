'''
Lists                            Set                                      Tuple
Mutable	                       Mutable	                                 Immutable
ordered                      unordered                               Ordered collection
collection of                 collection                                 of items
items                        of items                                       
Items in list               items in sets                         items in tuple can't be changed 
can be replaced           can't be replaced or changed            or replace 
List = [10, 20, 14] 

 
'''
#List--
List = [10, 20, 14]
print(type(List))
mylist = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
list=[1,'hello',4.5, "A"] 
list2=[1,2,3,4,5]
list3=[1,[1,2,3,],4,5,6]
print(list3[1])
print(list3)
print(list[:2]) # slicing of the index 
print(list[2:])
print(list, sep=" ")
list.insert(len(list), 6)
list.insert(0,12)
list.append(6)  
''''second method of the inserting the number so The append function appends a single item without having 
to specify the index.'''
list.extend([7,8,9,10]) # another function for addding the multiples item and extending the two lists
list.extend(mylist) 

#Deleting the item from the lsit :
list.pop(1)
#list.remove([2])

#del list(5)
'''for x in list:
    print('value',x)
print(list)
'''
#sorting the list
print('/n Sorting the lists')

nums = [1,3,45,5,6,23]
courses=['Math','Eng', 'Science','Computer']
nums.sort(reverse=True)
courses.sort(reverse=True)
print(courses)
print(nums)
# By using the function 
sorted_nums =sorted(nums)
print(sorted_nums)
''' we also can se min(), max() , sum()'fun on the lists'''

#finding the index of value
print(courses.index('Eng'))
                          #enumerate  for the index value
for index,course_name in enumerate(courses):
#for index,course_name in enumerate(courses, start=1): 
#index and course_name is the just varribale name
    print(index,courses)

#converting  the list into str and spliting the str into list
course_str ='-'.join(courses)
new_course_list = course_str.split('-')

print(course_str)
print(new_course_list)

############################################################################################################

#Examples of tuples:
'''We cant modifiy the tuples'''

Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)
print(Tuple1[0])
#Tuple: 
my_tuple=(1,'tuple',6.45,'name',True)
print(my_tuple[1])   # we can declare tuple without using the paranthesess
my_tuple1=1,'tuple',6.45,'name',True
print(type(my_tuple))
print(type(my_tuple1))

#concating the tuple
concat_tuple= (my_tuple1 + my_tuple)
print(concat_tuple)
print(my_tuple.count('tuple'))
#print(my_tuple.index('6.45'))
#for x in my_tuple:
 #   print(x)
#assigninng the value to the tuple
#my_tuple[0]=5    #It will not assign the value because anything that is in the tuple is immuteable


#########################################################################################################################################
#Set: 
set_1={1,2,3,4,5,5,'new'}
print(type(set_1))
print(set_1)
set_1.add(6)
set_1.remove(2)
set_1.discard(3)
# Set is not ordered
print(set[0])
# generate the type error and says that set are not in 
# sequnce it doesn't contains the all ordered index of all elements
set2={1,2,3,4,45,6,'new','old'}
print(set_1.intersection(set2))
print(set_1.difference(set2))
print(set_1.union(set2))

#creating the empty sets
empty_set = {} #this is empty list
empty_set=set()

'''
import array
arr=array.arr("f",(1,3,4,5,6,5.34))  #defining array of type float and  min size 4 bytes
arr[0]
print(type(arr))
#https://www.educative.io/answers/what-are-type-codes-in-python
#array.arr('typecode',[array, intializer])

"""array(typecode [, initializer]) -> array
Return a new array whose items are restricted by typecode, 
and initialized from the optional initializer value, which must be a list, string or iterable 
over elements of the appropriate type.
Arrays represent basic values and behave very much like lists, 
except the type of objects stored in them is constrained. 
The type is specified at object creation time by using a type code,
which is a single character. The following type codes are defined:"""

'''

################################################################################################################

#Dictionary

#Dictionary: Dictionary acceess the value on the base of the key and value
#  not on the index position of the value, so they are faster and more flexible 
#key: value
dict1 = {1:'coffe',2:1, 3:'tea'}
print(dict1[1])
dict1[3]='juice'#adding/or replacing the item in the dictionary 
print(dict1)
#del dict1([2])

#Iteration and other dictionary function in more details 
my_dict={1:'string', 'value':'new'}
my_dict[2]= 'test'
print(my_dict['value'])
print(my_dict)

#Updating the the dictionary 
#dict1.update({1:'Tea','name': 'JP','phone':567890})
print(dict1)

del dict1[3]
value=dict1.pop(2)
print(value)
print(dict1)

for key in my_dict:
    print(key) # this only printout the key
# for accessing the both we may to use the 'item'  function  
for key, value in my_dict.items():
    print(str(key)+ ' : '+ value)   #by using the some concatatination

print(my_dict.keys())
print(my_dict.items())
print(len(my_dict))