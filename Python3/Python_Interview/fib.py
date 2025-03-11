def fib(n):
    a,b=0,1
    if n ==0:
        print("Enter the value greater than 0",a)
    elif n ==1:
        print(a , b, sep="\n")
    else:
        print(a,b, sep="\n")
        for i in range(2,n):
            c= a+b
            a=b
            b=c
            #for upto 100 nums fib
            # if c<=100:
            #   break
            print(c)
n = int(input("Enter the Num for fib "))
fib(n)

#2. Recursive Method

def recursive_fib(n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-1)+ recursive_fib(n-2)

def print_fib(n):
    for i in range(n+1):
        print(f"fib at {i} is {recursive_fib(i)}")        

n = int(input("Enter the num "))
#recursive_fib(n)
print_fib(n)


#  iterative Method
def iterative_fib(n):
    a,b=0,1
    print(a)
    for _ in range(n):
        a,b = b, a+b
        print(a)
    return a


n = int(input("Enter the Num for fib "))
iterative_fib(n)
#print(iterative_fib(n))
