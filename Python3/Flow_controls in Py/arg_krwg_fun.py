#use of the args: 
#1).with args you can pass any amount of the non-keyword varriablels, like tuples  
#2). With kwargs you can pass any amount of keyword(var in key.) arguments, like dictionary

def sum_of1(a,b):
    return a+b
print(sum_of1(4,5)) 
#print(sum_of(4,5,6)): by using the three number it  will give the error so we have to use the args where number of agrument can be used
#
def sum_of(*args):
    sum=0
    for x in args:
        sum += x
    return sum  # need to use the return in the line of the loop
print(sum_of(4,5,6,7))

#--------------------------------------------------------------
 # Use of the kwargs

list= {'Tea':2, 'coffe':35}
def sum_of2(**kwargs):
    sum=0
    for k, v in kwargs.items():
        sum += v
    return round(sum,2)  # need to use the return in the line of the loop
print(sum_of2(coffe=4.52,tea=5.20,milk=62,mango=70))

def sum1(**kwargs):
    sum=0
    for i, i in kwargs.items():
        sum += i
    return round(sum,2)   
print(sum1(tea=2,coffe=5)) 


# Use of the both fun 

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses ={'Math', 'Art', 'science'}
info = {'name': 'john', 'age':23}

student_info(courses,info)
student_info(*courses,**info) #Adding the * for the unpacking the these dictionries values of this function
