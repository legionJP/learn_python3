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
        for j in range(i+1):
            print("*", end=" ")
        print()
    

