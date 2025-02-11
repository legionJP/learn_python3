'''
1. Pattern Solving Approach :
-> Outer loop will count the  no of lines 
-> Inner loop : focus on the column and connect them with rows 
    -> Inner For Loop:  Pattern Printing , * #
    -> Observe Symmetry (Optional)
-> Observe the Symmetry (in some cases)

'''
# Pattern 1:

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
