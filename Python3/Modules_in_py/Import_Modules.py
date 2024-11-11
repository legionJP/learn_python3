
from Import_fun import find_index as f_i , test
Course_list=['Economy','History','Plity','Science']
index=f_i(Course_list,'History')
print(index)
print(test)

import sys
print(sys.path) #finding the path of the file and modules
#from Import_fun import *

# if the path of module is not found we can add them manualy 
#1.
import sys
sys.path.append('/Users/jp/Desktop/Import_Modules.py')

#2. by the python environment changes , adding the python file path as a enironment

