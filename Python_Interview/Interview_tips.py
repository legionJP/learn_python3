
#===================================================================================#
# 10 different things you should know before going in to your first Python interview.
#====================================================================================#
#for entry level

#-----------------------------------------------------
#1.Know how to write the code on Paper or white board
#----------------------------------------------------

#-----------------------------------
#2. Know the Basic Control Flow :
#------------------------------------

for i in range(1,11):
    print(i)
 
i = 1 
while  i<= 10:
    print(i)
    i+=1
a= 10
b=20

if a<b:
    print("{} is less than {}".format(a,b))
elif a==20:
    print("{} is equal to {}".format(a,b))
else:
    print("{} is greater than {}".format(a,b))        

#------------------------------------------------------------
# 3. Able to Discus How you have used Python In Past Projects :
#-------------------------------------------------------------

# be ready with the your project , which is interesting 
#like webscraping project for weather info .

#or finding the file with .jpg extentsions
import os , glob
os.chdir("/Users/jjpsi/Documents")
for file in glob.glob("*.jpg"):
    print(file)


#------------------------------------------------------------
# 4. Know How to Solve Common Interview Problems:
#-------------------------------------------------------------

#1. FizzBuzz()
for num in range(1,50):
    if num%5 ==0 and num %3 == 0:
        print('Fizzbuzz')
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 ==0:
        print('Buzz')    
    else :
        print(num)

 #Fibonacci Sequence 

#Using the for loop

a,b = 0,1
for i in range(0,10):
    print(a)
    a,b  =b,a+b
    
 #------------
 # By recursion
 #---------
n= int(input("Type your terms for fibonaci: "))
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2) 
print(f"fibonaci numbers total at position {n}: is {fib(n)}") 

print("fibonaci Seqence :")
for i in range(n):
    print(fib(i))


#------------------------------------------------------------
# 5. Know  the Basic data Types : 
#-------------------------------------------------------------

#1. iterates the list
#2, iterate the tuple 
#3. Iterate the Dict
my_dict = {'name': 'Yash', 'age': 22, 'Occupation': 'Eng'}
for key,val in my_dict.items():
    print(" My {} is key and my value is {}".format(key,val))

#4. iterate the set
my_set = {1,2,3,4,5,6,77,6}
for i in my_set:
    print(i)



#------------------------------------------------------------
# 6. Know  How to Use List Comprehensions : 
#-------------------------------------------------------------
my_list= [1,2,3,4,5,6,77,6]

squares = [num * num for num in my_list]
print(squares)


#------------------------------------------------------------
 # 7. How to Use the Generators
 #-------------------------------------------------------------

#fibonaci Using the generator 

num= int(input("Type your terms for fibonaci: "))
def fib(num):
    a, b =0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1,a)
        a,b = b, a+b

for item in fib(num):
    print(item)


#------------------------------------------------------------
 # 8.  Know the Basics Of OOPs :
 #-------------------------------------------------------------

# Know the general templete for class
# declaratio of instances

##------------------------------------------------------------
 # 9. Have Py related Interview Questions to aks interviewr
 #-------------------------------------------------------------

#also prepared for the follow up questions if you are asking the questions 

#------------------------------------------------------------
 # 10. Know the Basics of other Technologies
 #-------------------------------------------------------------

#git 
#cl
#linux
#Sql
#other imerging tech.

#-------------------------
# #Tshape Tehnologies :
#------------------------

# The concept of T-shaped skills, or T-shaped persons is a metaphor used in job recruitment
# to describe the abilities of persons in the workforce. The vertical bar on 
# the letter T represents the depth of related skills and expertise in a single field, whereas the horizontal bar is
# the ability to collaborate across disciplines with experts in other areas and 
# to apply knowledge in areas of expertise other than one's own


#================================SUMMARY===============================#

# 1. Know how to code on whiteboard/white paper.
# 2. know the control flow in python like loops, if statement, switch statement etc
# 3. Know the basic built-in data structure like list, tuple, dictionary also know how and when to use them.
# 4. Be able to discuss how you've used python in your projects
# 5. Fundamental problems in python(based on data structures and algorithms)
# 6. Know how to use list comprehension, why it is fast?
# 7. Know how to use generators(Why generators are efficient?)
# 8. Learn basics of Object Oriented Programming.
# 9. Prepare some question for the interviewer.
# 10. Know some other fundamental technologies like git etc.