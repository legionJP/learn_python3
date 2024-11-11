'''
#file Writing operations

f = open('text2.txt','w')
f.write("Some content insdie the file will appear here")
f.close()
'''
#-------------------------------------------------------------------------
# or using the context manager like with statement lik it close the file automatically 

# with open('text2.txt','w') as f:
#     f.write ('This is inside conntent of the file.')

#-------------------------------------------------------------------

# Writing own context Manager 
#--------------------------------------

#1. By using the class 

class open_file():
    def __init__(self,destin_file, mode):
        self.destin_file = destin_file
        self.mode = mode

    def __enter__(self):
        self.file = open(self.destin_file,self.mode)
        return self.file

    def __exit__(self, exception_type, exception_val , traceback):
        self.file.close()

with open_file('text2.txt','w') as f1: # f1 is file object
    f1.write('Tsting the file')

print(f1.closed)    

#Using the function 

from contextlib import contextmanager

@contextmanager
def open_file1(file1 , mode1): # generator fun
    try:
        f2 = open(file1, mode1)
        yield f2  # it every will do like a class  __enter__ ,method 
    finally:
        f2.close()

with open_file1('text2.txt','w') as f2: # f1 is file object
    f2.write('Testing the file with function method')

print(f2.closed)

#open is alreadyy acontext manger 
#---------------------------------------------------------------------------------------

import os 
from contextlib import contextmanager
'''
cwd = os.getcwd()
print(cwd)
os.chdir('file_handlings_Py')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
print(cwd)
os.chdir('file_handlings_Py')
print(os.listdir())
os.chdir(cwd)

'''
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield 
    finally:
        os.chdir(cwd)    

with change_dir('/home/jp/Downloads/Os_Intro'):
    print(os.listdir())  

with change_dir('/home/jp/Downloads/learn_python3'):
    print(os.listdir())          