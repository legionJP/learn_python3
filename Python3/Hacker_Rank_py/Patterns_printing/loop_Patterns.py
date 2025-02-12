'''. Pattern Solving Approach :
-> Outer loop will count the  no of lines 
-> Inner loop : focus on the column and connect them with rows 
    -> Inner For Loop:  Pattern Printing , * #
    -> Observe Symmetry (Optional)
-> Observe the Symmetry (in some cases)

'''
# Pattern:

row=5
# row = int(input())
for i in range(row):
    for j in range(row):
         print("* ", end="")
    print()

# Pattern 2:

def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1): # (j=0, j<=i, j++)
            for j in range(i):
             print("*", end=" ")
        print()
nForest(4) 

# Pattern 3

def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):  # (j=1, j<=i, j++)
            print(j+1, end=" ") # or can start the j=1 , as the initial value for print(j,end=" ")
        print()
nTriangle(4)

#  Pattern 4

def triangle( n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=" ")
        print()
triangle(4)

# Pattern 5

def seeding(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        for j in range(i,n):
            print("* ", end="")
        print()

seeding(4)

# Pattern 6
# Reverse the number 

def reverse_num(n):       
    for i in range(n):
        for j in range(i+1,n+1):
            print(j-i, end=" ")
        print()

reverse_num(3)


# pattern 7
# print the space, star, space
#            s s * s s # 2 space, 1*
#            s * * * s # 1 space , 3*
#            * * * * * # 0 ,        5*
# (n-i-1)(2*i+1) (n-i-1)
#  loop1,,2,,,,,,,3
#   *
#  ***
# *****

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(0,2*i+1):
            print("*", end="")
        for l in range(n-i-1):
            print(" ", end="")
        print()
nStarTriangle(4)

print("---------------------------------------")

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for k in range(i):
            print(" ", end="")
        for j in range(i+1,2*n-i):
                print("*", end="")       
        for l in range(i):
            print(" ", end="")
        print()
nStarTriangle(4)

'''
* * * * 
 * * *
  * * 
   *
'''
print("---------------------------------------")

def nStarDiamond(n: int) -> None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(0,2*i+1):
            print("*", end="")
        for m in range(n-i-1):
            print(" ",end="")
        print()
    for i2 in range(n):
        for j2 in range(i2):
            print(" ", end="")
        for k2 in range(i2+1,2*n-i2):
            print("*", end="")
        for m2 in range(i2):
            print(" ", end="")
        print()
nStarDiamond(4)


print("---------------------------------------")
# find the symmentry , for n =5 rows the pattern repeat itself 
# so , rows = 2*n-1 = 9
# i =1
'''
*
**
***
****
***** : 5 ==> num of star: i+1==> 4+1
****  : 4 ==> 2*n-i ==> 2*5-6= 4
***   : 3 ==> 2*n-i==> 3
**    : 2 ==> 10-8 =2
*     : 1
'''
def nStarTriangle(n: int) -> None:

    # Write your code here.
    for i in range(2*n-1+1):
        stars=i
        if i>=n:
            stars=2*n-i
        for j in range(stars):
            print("*", end="")
        print()
nStarTriangle(5)

print("---------------------------------------")

# nBinaryTriangle:
'''
n=4
1
0 1
1 0 1
0 1 0 1
'''

def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(4):
        if i%2 ==0: # if i=even start value is 1  else start =0
            start=1
        else:
            start=0
        for j in range(i+1):
            print(start,end="")
            start = 1-start
        print()

nBinaryTriangle(4)

print("---------------------------------------")
# Middle spcae is 2*(n-1)


def numberCrown(n: int) -> None:
    space = 2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")

        # space 
        for l in range(space):
            print(" ",end=" ")

        for k in range(i+1,0,-1):
            print(k, end=" " )
        print()
        space -=2
        

numberCrown(6)
print("---------------------------------------")
# Increasing Number 
def nNumberTriangle(n: int) -> None:
    num=1
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num= num+1
        print()
nNumberTriangle(5)

print("---------------------------------------")

def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    # string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # for i in range(n):
    #     for j in range(i+1):
    #         print(string[j],end=" ")
    #     print()

    # using the ord and chr 
    for i in range(n+1):
        # char = [ch='A'+i for ch in char]    
        for j in range(ord('A'),ord('A')+i):
            print(chr(j), end=" ")
        print()
nLetterTriangle(5)


print("---------------------------------------")
# Reverse nLetterTriangle

def nLetterTriangle(n: int):
    # Write your solution here.
    
    for i in range(n):
        for j in range(ord('A'),ord('A')+(n-i)):
            print(chr(j), end=" ")
        print()
nLetterTriangle(5)
    
print("---------------------------------------")


def alphaRamp(n: int) -> None:
    # Write your solution from here.
    for i in range(n):
        char = ord('A')+i
        for j in range(i+1):
            print(chr(char), end=" ")
        print()
   
print("---------------------------------------")
'''
    A
  A B A
A B C B A

PATTERN of the chars: after  (2*i+1)/2, it goes into breakpoint and reverse 
 the char 
'''

def alphaHill(n: int):
    # Write your solution from here.
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")

        # characters
        breakpoint = (2*i+1)//2 
        ch = ord('A')
        for p in range(0,2*i+1):
            print(chr(ch), end="")
            if p < breakpoint:
                ch+=1
            else:
                ch-=1
        # for j in range(n-i-1):
        #     print(" ", end="")
        print()

alphaHill(3)    
    
# Approach 2    

# def alphaHill(n: int):
#     # Write your solution from here.
#     for i in range(n):
#         # Print leading spaces
#         for j in range(n-i-1):
#             print(" ", end="")

#         # characters in increasing order
#         ch = ord('A')
#         for p in range(0, i+1):
#             print(chr(ch), end=" ")
#             ch += 1
        
#         # characters in decreasing order (reverse of increasing)
#         ch -= 2  # Adjust after the last increment
#         for p in range(i-1, -1, -1):
#             print(chr(ch), end=" ")
#             ch -= 1
        
#         # Move to the next line after each row
#         print()

# # Test the function
# alphaHill(5)


# print('----------------------------------------------------------------------------------')
def alphaTriangle(n: int):
    # Write your solution here.
    for i in range(n+1):
        char = ord('A')+n-1
        for j in range(char,char-i,-1):
            print(chr(j), end=" ")
        print()
alphaTriangle(3)

#
'''
For every value of ‘N’, return the symmetry as shown in the example.
Example:

Input: ‘N’ = 3

Output: 
* * * * * * 
* *     * * 
*         * 
*         * 
* *     * * 
* * * * * * 

'''

