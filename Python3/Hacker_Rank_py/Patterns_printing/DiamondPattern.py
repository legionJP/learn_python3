
row = int(input("Enter the number of rows: "))
for i in range(row, 0 ,-1):
    for j in range(i):
        print("* ", end="")
    print()
for i in range(2, row+1):
    for j in range(i):
        print("* ", end="")
    print()

# Printing the Diamond:

row = int(input("Enter the number of rows: "))
# Upper part of the diamond
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
# Lower part of the diamond
for i in range(row - 2, -1, -1):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * * 
# * * * * *
