
#                                      Operator in Python3
# -----------------------------------------------------------------------------------------#
# Airthmetic operator 
# Assignment operator 
# Relational operator 
# Logical operator 
# Unary operator 

# 1. Airthmetic Operator 
x= 1
y=2
print(x+y) 

# 2. Assignment
x= 2 # it is Assigment

x= x+2 #Adding the value 2 in the x 
print(x)
x += 2  # same but  this is like increment of 2 in the value x
print(x)
# Also --
x *=2
x/=2
print(x)

# 3 Assigning the multiple value 
a, b = 3,4

#------------------------------------------------------------------------
# 2. Unary Operator ----> one 
#-------------------------------------------
n = 12
n =-n
print(n) #it will be minus value

#------------------------------------------------------------------------
# 2. Relational Operator
#---------------------------------------------------------------
print(a<b)

print(a==b) 
a=4
print(a==b,a<=b,a>=b,a!=b)

#------------------------------------------------------------------------
# 2.  Logical Operator
#------------------------------------------------------------------------
# 1. AND
a= 12
b= 13
print(a<15 and b<14) 
print(a>15 and b<15)
print(a<15 and b>16)

# 2. OR
print(a<15 or b<14) 
print(a>15 or b<15)
print(a>15 or b>16)

# 3. NOT
x = True
print(x)
X = not x
print(X)