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
        for j in range(i):
            print("*", end=" ")
        print()
    

# Pattern 6
# Reverse the number 

def reverse_num(n):       
    for i in range(n):
        for j in range(i+1,n+1):
            print(j-i, end=" ")
        print()

reverse_num(3)