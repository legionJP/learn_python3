#-----------------------------------------------------------------------------------------#
#                         Fibonacci
#-----------------------------------------------------------------------------------------#

# Fib = 0,1,1,2,3,5,8,13,21... (starts from 0, 1)
def fib(n):
    a,b=0,1
    if n<=0:
        print("Enter the number greater to 0 or postive num: ")
    elif n==1:
        print(a,b,sep="\n")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c= a+b
            if c>100: # for the last number in fib to be less than hndered
                break
            a=b
            b=c
            print(c) 
n= int(input("Enter the Number to find the fib series: "))              
fib(n)

#-----------------------------------------------------------------------------------------#
#                              Factorial 
#-----------------------------------------------------------------------------------------#

# Find the factorial 5 = 1*2*3*4*5 =120 --> (n*n-1)

# Looping solution to find factorial

x = int(input("Enter num to find the fact: "))

def fact(x):
    if x<=0:
        return 0
    else:
        f =1
        for i in range(1,x+1):       
            f=f*i
        return f    

result = fact(x)
print(result)

#-----------------------------------------------------------------------------------------#
#   Recursive solution to find the fact
#-----------------------------------------------------------------------------------------#

n= int(input("Enter the number for fact. "))
def find_factorial_recursive(n):
    if n==1:                  # Base condition
        return 1
    else:
        return n*find_factorial_recursive(n-1) 
# here retrun is keeping the reference of implemented value and calling again and again 
print(find_factorial_recursive(n))  
