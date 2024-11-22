# Create the 4 function as a Modules or separate modules for adding subtrating and more

#1.
import calc # Importing the calc module for add , mul, div 
s= calc.add(9,7)
print(s)

#2.
from calc import add, sub, mul , div
print( mul(9,7))
