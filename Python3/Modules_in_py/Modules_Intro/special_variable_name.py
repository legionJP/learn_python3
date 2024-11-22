#----------------------------------------------------------------------------------------------#
#                        Special Variable:  __name__
#----------------------------------------------------------------------------------------------#

#The first Module is Always Main which is in python __name__
#
# print(__name_)
print("hello" + __name__) # it is hello main wihout importing the calc

import calc
print("svn's hello" + __name__) 

'''
It will print name of calc module nameor anything in it bcz we are importing calc iand __name will print main 
So the _name_ var changes according to the file and module
'''

#----------------------------------------------------------------------------------------------#
#                       Use of the __name__ = "__main__"
#----------------------------------------------------------------------------------------------#

'''
I have build the fun here and import the this file as module in the calc and when I run the 
calc it prints all the satements or execute the function  in the calc as moudlue
To avoid this and only print the below satement or function pu it in the main block with special
method __name__ and call it with if condition , run the this code and then the calc file code 
now the calc file only execute the calc file's code, Yes comment the aboe code to use this one
'''

# So it as the start of the code or only execute ones
def main():
    print("Hello")
    print("Welcome User",end="")

#main()
if __name__ == "__main__":  # Thi means if this is the file we are running then __name__ will hold main
    main()
#----------------------------------------------------------------------------------------------#
'''
# Example 2
from calc import add
def fun():
    add()
    print("fuunc1")
def fun1():
    print("func2")

def main():
    fun()
    fun1()
main()        
'''

#----------------------------------------------------------------------------------------------#

