# Already Describes in detailed in the Functional Programming


Nums= [1,2,3,4,5,6,7,8,9,10,11,12]

#If you wan t'n' for each 'n' in nums 
Num_list =[]
for n in Nums:
    Num_list.append(n)
print(Num_list)

# By using the list comprehension
Num_list = [n for n in Nums]
print(Num_list)


# for n*n for each 'n ' in Nums:
'''
Num_list =[]
for n in Nums:
    Num_list.append(n*n)
print(Num_list)

'''
#By using th elist Comprehension
Num_list =[n*n for n in Nums]
print(Num_list)


#Using the Lambda + Map function

Num_list1 =map(lambda n: n*n, Nums)
print (Num_list1)

# for 'n' for each n in nums i fn is even

Num_list=[]
for n in Nums:
    if n%2 ==0:
        Num_list.append(n)
print(Num_list)

#By Using the Filter and Lambda function
Num= [1,2,3,4,5,6,7,8,10]
Num_list1=filter(lambda n: n%2 == 0, Num) 
print(Num_list1)#printing the location o f filter object !

#By using the list COmprehension
Num_list1=[n for n in Num if n%2 ==0]
print(Num_list1)

# if  wewan ta (letter, num ) pair fo each letter in 'abcd ' and each number in '0123'
Num_list =[]
for letter in 'abcd':
    for num in range(4):Num_list.append((letter,num))
print(Num_list)    

#By  using the list comprehension
Num_list =[(letter,num) for letter in 'abcd' for num in range(4)]
print(Num_list)


# DIctionary comprehension 
names =['JP', 'AK', 'MM', 'DP', 'Wade']
Department=['IT', 'food', 'Trade','Security', 'paav']
#print(zip(names,Department))
my_dict = {}
for names , Department in zip(names, Department):
    my_dict[names]=Department #here names is the key and Department is value
print(my_dict)

my_dict1={name: Dept for name, Dept in zip(names,Department)}  #not working!
print(my_dict1)


#Set Comprehensions
nums =[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)

#type 2 
my_set ={n for n in nums}
print(my_set)


#Generator Expression

#  I want to yield n*n for each 'n' in nums
nums=[1,2,3,4,5,6,7,8,9,10]

def gen_fun(nums):
    for n in nums:
        yield n*n
my_gen =gen_fun(nums) 
#my_gen =(n*n for n in nums)
for i in my_gen:
    print(i)   
