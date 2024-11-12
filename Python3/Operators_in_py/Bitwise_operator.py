
# Bitwise Operator : 
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
# 2. Bitwise ANS (&)
#----------------------------------------------------------------------
