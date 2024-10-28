#Coding Problemsa for the python: 
# it is dynamically typed and can assign the run time also 
n = 0
n= 1
n= n+1 
#None is null 
n= None
# we use the indentation 
# Paranthese is used for multiple line conditions
n= 5
print(4)
print(-10%3)
import math 
print(math.fmod(-10,3))

# array 
arr = [1,2,3]
print(arr)
arr.pop()
arr.append(5)

arr.insert(1,7)
print(arr)
arr = [1] *n
arr[0] =0  # not the o(n)


#===================================================================================#
# Fibonacci problems 
# 0 1 1 2 3 5 8 13 21......
#===================================================================================#

f_num = int(input("enter your number "))

def fib_func(f_num):
    if f_num <= 1:  # checking if the number is less than or equal one 
        return f_num
    return fib_func(f_num-1)+ fib_func(f_num-2) # adding logic for fib num calculation at every term or iteration 
print(f" total term in fibonacti  for number  {f_num} will be {fib_func(f_num)}")    
print("Fibonaci sequence is: ")

for i in range(f_num):   # iterating the func every time in the its range , like 1-4 
    print(fib_func(i))

#==================================#
#   Using the loop 
# #================================#  
# here first the n1 , n2 will print 0, 1 
# when input is grater than 3 than it will be range of 2-3 than n3 = 1 , and n1 = 1 , n2 = 1
# than print the n3 and , result will be 0 ,1 ,1 
# 0 1 1 2 3 
input_fibn =  int(input("enter your fib number "))
n1, n2 = 0,1 
print('fibonacci series using loop is:', n1, n2, end=" ")
for i in  range(2, input_fibn):
    n3 = n1+n2 
    n1 = n2
    n2 = n3 
    print(n3, end=" ")

# n3 = n1+n2 
# n1= n2 #(0 ---> 1)
# n2 = n3 #(1-->2)
# print(n3)
print()    
#=========================================================================================#
                               #Q2:  for reversing the number 
#=========================================================================================#
#Q2:  for reversing the number 
# input 
# then condition if num is less than 0 
# now take the modulu of num  r_mod= rev_input%10
# store the modulo in var rev_r with the reverse_num1 = reverse_num1*10+ r_mod = 42= 2*10+2
# than make the floor devision to remove the remainder 
# print the result with the reverse

rev_input = int(input("enter num for the fib series "))
reverse_num1 =0 
tmp =rev_input
while rev_input>0:
    reminder1= rev_input%10 # to extract the last number 
    reverse_num1 = reverse_num1*10+reminder1



    rev_input = rev_input//10
print(reverse_num1)    

print("the given number is {} and the revers order is {}".format(tmp, reverse_num1))

print(60//10) #(result of division)

##========================================================================================# 
                                    #Q3:  Find the gratest common divisor 
#=========================================================================================#
 # if n1 = 4, and n=10 than gcd =2 
 # first take two input 
 # than comapre tham and find small num 
 # than take the common range to divide the number like range(1, smallnum+1 )
 # than check the mudulus of the both in every iteration which will link (i%num1 = 0) and (i%num2=0)
# so the gcd will be i 

gcd_num1 = int(input("Enter your first num"))
gcd_num2 = int(input("enter your second number"))

def gcdFunctiopn(gcd_num1, gcd_num2):
    gcd =0 
    if gcd_num1 < gcd_num2:
        small_num = gcd_num1
    else:
        small_num = gcd_num2

    for i in range (1, small_num+1):
        if(gcd_num1%i == 0) and (gcd_num2%i==0):
            gcd = i
    print("the gcd of the two number is {}".format(gcd))        

gcdFunctiopn(gcd_num1, gcd_num2)         

#======================================================================================#
                          #Q4 =  Finding the perfect number       
# =====================================================================================#

#  6 is a perfect number because its proper divisors are 1, 2, and 3, 
# and we have (1 + 2 + 3 = 6).
# take the input 
# then iterate it  to the range of the 1 to num ,and if the num%1==0 than 
# take temp = 0  and add the value of if the muduols is 0 ao temp = temp+i
# than compare the number if temp == n , than its a perfect number 

num= int(input("enter your number to check it for perfect number "))
temp= 0

for i in range(1, num):
    if num%i == 0:
        temp = temp+i
if temp == num:
    print("the num {} is a perfect num".format(num))
else:
    print("the num {} is not a perfect number".format(num))        
#=======================================================================================#
                      #check if the string is palindrome or not 
#=========================================================================================#

# take the string iput 
#than apply the string reverse slicing 
#compare the both 

string1= input("Enter the your string: ")
string2 = string1[::-1]

if string1 == string2:
    print('the string {} is a palindrome string'.format(string1))
else:
    print('it is not palindrome string')

#=======================================================================================#
#take user input
String = input('Enter the string :')
#take character input
Character = input('Enter character :')
#initiaalize int variable to store frequency
frequency = 0
#use count function to count frequency of character
frequency = String.count(Character)
#count function is case sencetive 
#so it print frequency of Character according to given Character
print(str(frequency) + ' is the frequency of given character')

#============================================================================================#

# 13. Write a code to replace a substring in a string.
 #Python
string=input("Enter String :\n")
str1=input("Enter substring which has to be replaced :\n")
str2=input("Enter substring with which str1 has to be replaced :\n")
string=string.replace(str1,str2)
print("String after replacement")
print(string)


#====================================================================#
  
# . Write a code to Sort the element of the array without sort method
#====================================================================#


# def the func for the desc order
# wirte the code in ascenig or descending order 
# use of the neted loop ,
# where put the iteration for the range of the len of the array , iside the nested loop  
# from i+1 to range of the array
# than comapre the set of arrays q to sort them  

def sort_asc(arr1):
    for i in range(len(arr1)):  # every time checks the term 
        for j in range(i+1, len(arr1)): # check the second term to the lenght  of the arr
            if arr1[i]>= arr1[j]: # comapre them if statisfy 
                arr1[i], arr1[j] = arr1[j],arr1[i] # swap the arr valuse to reorder in ascending order 

numb_arr = [65, 231, 145,90,43,23]
sort_asc(numb_arr)
print("sortest list with ascending orderr is:",numb_arr)

#=========================================================
# Taking the nth number of array as a input from the users
#===========================================================
n = int(input("Enter the number of elements in the array: "))
array_values = list(map(int, input(f"Enter {n} values separated by spaces: ").split()))
nth_index = int(input("Enter the index (0-based) of the value you want: "))
if 0 <= nth_index < n:
    nth_value = array_values[nth_index]
    print(f"The {nth_index+1}th value in the array is: {nth_value}")
else:
    print("Invalid index. Please enter a valid index.")

                       
                       
#=============================================================================#

#  Write a Program to Add two Fractions
# Program in C	Program in C++	Program in JAVA	Program in Python
def findGCD(n1, n2):
gcd = 0
for i in range(1, int(min(n1, n2)) + 1):
if n1 % i == 0 and n2 % i == 0:
gcd = i
return gcd


# input first fraction
num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))

# input first fraction
num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))

lcm = (den1 * den2) // findGCD(den1, den2) #floor divioson with the greatest common divisor 

sum = (num1 * lcm // den1) + (num2 * lcm // den2)

num3 = sum // findGCD(sum, lcm)

lcm = lcm // findGCD(sum, lcm)

print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", lcm)
#===================================================================================#

# Write a Program to Find the Factorial of a Number using Recursion.
# Program in C	Program in C++	Program in JAVA	Program in Python
def factorial(n):
if n == 0:
return 1
return n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))
#===================================================================================#

# Write a code to find Fibonacci Series using Recursion