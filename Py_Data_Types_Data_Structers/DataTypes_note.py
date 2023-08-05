#Data_Types=
#1.Numereic- Integer, Float, Complex Number
#Sequence-String, List, Tuples:
#->.String is a sequence of characters that is enclosed in signle or double quotes.

#List: List are essentially an array and hold any type data inside square bracktes :
list=[1,'hello',4.5, "A"] 
list2=[1,2,3,4,5]
list3=[1,[1,2,3,],4,5,6]
print(list3[1])
x=enumerate(list3)
print(x)
print(list3)
print(list, sep=" ")
list.insert(len(list), 6)# 1st method of inseritng item str a specified index
list.append(6)  #second method of the inserting the number so The append function appends a single item without having to specify the index.
list.extend([7,8,9,10]) # another function for addding the multiples itemm
#Deleting the item from the lsit :
#    list.pop(1)
#     del list(5)
for x in list:
    print('value',x) #in a list x will run for the number of times of list's number. 
print(list)


#Tuples: values inside the tuple can't be modified or changed : tuple1=(1,'hello',8.9,"A")
#Dictionary- Dictionary store data in key value structure : dict={'a':22, 'b':44.4}
                                                            #print('a')
                                                            #22
#Boolean: type(true), type(false)
#set- example_set={1,'hello',4.5,"A"}

#Type Casting :  Process that convert the one data type into the another like : '123' string to int 123
#Types: 1.) Implicit: It is convereted automatically by the the python into a comptable data type which coverets int to float not string to int.
 
#2). #Explicit:this is done by the python function like : str(),: str(111)= '111', float() , int(2.05)

#other data type functions: ord(): integer into the underlying  unicode representative character ,
# hex(): converts integer to hexa decimal string , 
#oct(), tuple(), set(), list[], dict()


# Python's User control input and formating 
#Print argument and string concatenation
#Direct Fromating 
print("I like {0} more than the {1}".format("orange","mango"))

#Input / Output formating 
str1=input("please inter your first name ")
str2=input("please enter your last name ")
print("hello" + str1+ ' '+str2)

#Tuple: 
my_tuple=(1,'tuple',6.45,'name',True)
print(my_tuple[1])   # we can declare tuple without using the paranthesess
my_tuple1=1,'tuple',6.45,'name',True
print(type(my_tuple))
print(my_tuple)
#print(my_tuple.count('tuple'))
#print(my_tuple.index('6.45'))
for x in my_tuple:
    print(x)
#assigninng the vale to the tuple
#my_tuple[0]=5  
#   #It will not assign the value because anything that is in the tuple is immuteable

#Set: 

      
