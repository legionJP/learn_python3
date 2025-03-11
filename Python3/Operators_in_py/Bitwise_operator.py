#-----------------------------------------------------------------------
# Bitwise Operator : 
#------------------------------------------------------------------------
'''
--> Complement (~)
--> And (&)
--> Or (|)
--> XOR (^)
--> Left Shift (<<)
--> Right Shift (>>)

'''
#----------------------------------------------------------------------------
# Complement (~)-- tilde or NOT(~)
# --> complement to the reverse of the binary format 
#-------------------------------------------------------------------------
'''
Bitwise Complement Operation:
The bitwise complement inverts each bit.
Applying ~ to 5 (00000101) results in 11111010.

Two's Complement Representation:
In Python, integers are represented using two's complement notation.

In two's complement, the most significant bit (leftmost) represents the sign of the number (0 for positive, 1 for negative).

The bitwise complement 11111010 is interpreted as -6 in decimal due to two's complement rules.
'''
a = 5  # binary: 0101
result = ~a  # binary: 1010 (in 32-bit representation: 11111111111111111111111111111010)
print(result)  

print(~11)
print(bin(6))  # see the images for more explanations 

#--------------------------------------------------------------------------------------
# 2. Bitwise AND (&) and 3. OR (|)
#----------------------------------------------------------------------

print(12 & 13)

print(bin(12)) # ----> 00001100

print(bin(13)) # ----> 00001101 # doing And (&)
#__________________________________
  #And Operations ---> 00001100 ---> 12
  #OR Operations ----> 00001101 ---> 13  
  # XOR ----     ----> 00000001 --->  1  
print(13|12)
print(25 & 30) #----> 24

#-------------------------------------------------------------------------------------------------------#
# 4. XOR (^) -- 0 0 --> 0
#               0 1 --> 1
#               1 0 --> 1
#               1 1 --> 0  # if both the number is different you can go for the 1 

print(12 ^ 13)
#-------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------#
#   5. Left shift (<<) -- in this we gain the 2 bits towards the left
# 
#  10 -----> 1010.000 --> left shift 2 bits ---> 101000.000 ---> 40
# -------------------------------------------------------------------------------------------------------#

print(10 << 2) #---->40 
#-------------------------------------------------------------------------------------------------------#
#   5. Right shift (<<) -- in this we losse the 2 bits towards the right
# #-------------------------------------------------------------------------------------------------------#
print(10 >>2)