'''. Pattern Solving Approach :
-> Outer loop will count the  no of lines 
-> Inner loop : focus on the column and connect them with rows 
    -> Inner For Loop:  Pattern Printing , * #
    -> Observe Symmetry (Optional)
-> Observe the Symmetry (in some cases)

'''
# Pattern:

row = int(input())
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