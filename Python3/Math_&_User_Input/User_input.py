# -------------------------------------------------------------
#  Taking Input from the user
#--------------------------------------------------------------
x_str= input("tEnter the number") # By default input gives the string format

x= int(input("Enter the number "))
# x1 =int(x)
y= int(input("Enter the 2nd Number "))
z= x+y
print(z)

# only print the 1 char if multiple was entered
ch = input("Enter the character! ")
print(ch[0])

# Only fetch the 1st or one char by the input 
ch1 = input("Enter the char ")[0]
print(ch1)

# eval fun for evaluating the expression
ex = eval(input("Enter the expression "))
print(ex)

# Taking the full expression as input in command line , the file name is first or 0 index
# import sys
# x= int(sys.argv[1])
# y= int(sys.argv[2])
# z= x+y
# print(z)
