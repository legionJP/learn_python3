#---------------------------------------------------------------------------------------------------#
#                         Map , Filter , Reduce using  with the lambda
#---------------------------------------------------------------------------------------------------#
from functools import reduce

#1. Filter
#--------------------------------------
nums = [3,2,5,7,8,3,7,8,9]

def is_even(n):
    return n%2 ==0
    
evens = list(filter(is_even,nums)) 
print(evens)
# it will take the sequence will give the sequence ,
# here filter using the is_even function will iterate the nums list than print the evens

# Using the lambda 
evens =list(filter(lambda n: n%2==0,nums))
print(evens)

doubles = list(map(lambda n: n*2 ,evens))
print(doubles)

sum = reduce(lambda a,b :a+b, doubles )                      # import from functools
print(sum)

#---------------------------------------------------------------------------------------------------#
#                         Using the map function
#---------------------------------------------------------------------------------------------------#

country=['India', 'USA','Rusia','Africa','Bharat']

def find_in_map(country_name):
    if country_name[0] == 'I':
        return country_name
    
map_country=map(find_in_map,country) # first argu ment is function itself then the iterable item/     
print(map_country)                             #and here functions is not calling but using to give argument not 
for x in map_country:
    print(x)

#---------------------------------------------------------------------------------------------------#
#           Using the Filter Function
#---------------------------------------------------------------------------------------------------#
menu1=['asia', 'australia','North America','Antartica']

def find_in_world(continent):
    if continent[0]=='a':
        return continent
    
filetr_in_world=filter(find_in_world,menu1)

print(filetr_in_world)
for x in filetr_in_world:
   print(x)    


#Note:  Map() returns every item in an iterable 
# and filter() returns  all item  when functions returns   True.
#---------------------------------------------------------------------------------------------------#
#                        Paasinng the List to the Function
#---------------------------------------------------------------------------------------------------#

lst = [23,434,545,1,34,5,76,8,5,7,34]
def count(lst):
    even =0
    odd =0
    for i in lst:
        if i%2 ==0:
              even+=1
        else:
            odd+=1
    return even , odd

even , odd= count(lst)    # as func return the even and odd so we are using the two object to call  
print(even)   
print(odd) 
print("even count is {} and odd is {} ".format(even,odd))
