set_1={1,2,3,4,5,5}
print(type(set_1))
print(set_1)
set_1.add(6)
set_1.remove(2)
set_1.discard(3)

#Mathematical Operator in the sets
set_a={1,2,3,4,5,6,7,'rtst'}
set_b={2,3,4,5,6,7,8}
print(set_a.union(set_b))
#print(set_a | (set_b))u8
print(set_a.intersection(set_b))
print(set_a & set_b) # also for getting the intersection
#getting the difference from the sets
print(set_a.difference(set_b))  #this will get the differnece of the element which is only in the set a and not present in set b
print(set_a - set_b)
#getting the symmetrical difference 
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b) #also by the carret operator
 #the symmetric difference shows that all that elements that are present in the set a and set b but not a common elements

# Set is not ordered
print(set[0])
# generate the type error and says that set are not in sequnce it doesn't contains the all ordered index of all elements

#Dictionary: Dictionary acceess the value on the base of the key and not on the index position of the value, so they are faster and more flexible 
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
for x in my_dict:
    print(x) # this only printout the key
# for accessing the both we may to use the 'item'  function  
for key, value in my_dict.items():
    print(str(key)+ ' : '+ value)   #by using the some concatatination

