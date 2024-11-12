#about the conditionals and boolean statement

if True:
    print('coditon was true')
if False:
    print('condtion was false')



#comparisons Statement in Py

#Equal :   ==
#Not equal :  !=
#greater than : >, Less than: <
#Greater or equal: >= and Less or equal <=
#Object Identity: is
#and , or , not
    
language='java'
if language=='python':
    print('conditional was true')
elif language =='java':
    print("lang is java")
    #We can add multiple elif in place of the switch terminlogy     
else:
    print('Not Match')


user='Admin'
logged_in= True
if user=='Admin' and logged_in: 
#if user=='Admin' or loggrd_in:
#if not logged_in:
    #print('Please log in')
    print('admin page')
else:
    print('bad credentiels')
    #print('welcome')

a=[1,2,3,4,5]
b= [1,2,3,4,5]
c=[1,3,4]
d=[1,3,4]
print(a==b)
print(a is b) #print the false 
print(id(a))
print(id(b))
print(c is d)


#Condtion that evalutes False by the statment 

#False Values: 
#1. False
#None 
#Zero of any Numeric type 
#Any emmpty sequence ex. '' , () , {}
# Any empty mapping , for example, {} 
# Everything else will be evaluated to the true

condition=None
#condition ={}
#condtion =0 
if condition:
    print("it is evaluating true")
else:
    print('evaluated to False')    