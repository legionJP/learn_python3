'''
The OS module provides us a layer of abstraction between us and
the operating system. When we are working with os module always 
specify the absolute path depending upon the operating system 
the code can run on any os but we need to change the path exactly. 
If you try to 
remove a file that does not exist you will get FileNotFoundError
'''
import os
cwd=os.getcwd()
print("current working directory is",cwd)
print(dir(os))

#Chnage the curent working directory 

def current_path():
    print("current working directory  before is",cwd)
changedir=os.chdir('../')
current_path()
print("the new working directory is ", changedir)
print(os.listdir())

#Creating a directory
'''
os.makedirs('OS_Demo3/Os_types')# create the leaf directory 
os.removedirs('OS_Demo2/Os_types')
os.mkdir('OS_Demo/')  # used to create a directory named path with the specified numeric mode. This method raises
#FileExistsError if the directory to be created already exists.
'''

#Creating the directory by giving the path and joining lon th emain direcotry 

'''
directory ='Code_file' #to be created
parent_dir='/home/jp/Downloads/'
path = os.path.join(parent_dir,directory)
os.mkdir(path)
print("directory '%s' created " % directory)

#os.makedirs(path) 
 
#Super-mkdir; create a leaf directory and 
'''

#Renaming the directory

'''
#os.rename('OS_Intro', 'OS_Introduction')
import os 
from datetime import datetime
print(os.listdir())
print(os.stat('OS_Introduction'))
print(os.stat('OS_Introduction').st_size) # size of file in bytes
print(os.stat('OS_Introduction').st_mtime) #info aboiut the modified time
mod_time= os.stat('OS_Introduction').st_mtime
print(datetime.fromtimestamp(mod_time))  # human readbale time stamp

'''
#Notes

'''
all intermediate ones. Works like mkdir, except that
any intermediate path segment (not just the rightmost) will be created 
if it does not exist. If the target directory already exists, 
raise an OSError if exist_ok is False. 
Otherwise no exception is raised. This is recursive

print("directory '%s' created " % directory)

'''


# Using the genrator OS.WALK()

# this method goes through the all of the directories and files in that path  with  sub tree directories

for dirpath, dirnames ,filenames in os.walk('/home/jp/Downloads/learn_python3'):
    print('Curent path' ,dirpath)
    print('Direcotries:', dirnames)
    print('Files:',filenames)
    print()





'''
#Specified numeric Mode

mode should be specified in octal representation and 
therefore must begin with a 0o

#To change the permission of a 
#file, you can use the
os.mkdir(path, mode) 
print("Directory '% s' created" % directory) 
os.chmod(file, mode) 

0o666: used for the creating  the directory 
0o777: make a file readonly, you can set the permission to 0o777,
os.chmod( )
OS stat module  : 
os.stat()
lstat, fstat

'''

#os.listdir
path = '/'
dir_list = os.listdir(path)
print("files and direcotries in ' ", path,"' :")
print(dir_list)

#Removing the Directory 

'''
os.remove('/')
os.rmdir('/') #to remove the empty directory
os.remove(path)
os.rmdir(path)

'''

os.name
print(os.name)
#This function gives the name of the operating system dependent module imported. 
#The following names have currently been registered:
#‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’
os.error
#IO error

#Opening  and closing the file
'''
os.popen
file = os.popen('fd', 'w')
file.write("Hello")
os.close

'''
#os.remove('filename')


#Writing the file and closing of file
'''
file = os.popen('fd,' 'w')
file.write("Hello")
os.close(file)
os.rename('fd','new.txt')

'''

# checking the file existence
'''
os.path.exists("file_nmae")
os.path.getsize('file_name') #prints in the bytes
result = os.path.exists("file_name") #giving the name of the file as a parameter.
  
print(result) #true or false 

'''

#Checking the environment 
print(os.environ.get('Home/jp/Downloads/learn_python3'))

'''
#joining the file path 
file_path= os.path.join(os.environ.get('Home'),'text.txt')
print(file_path)

'''

# file manupulation with the os.path 

print(os.path.basename('/Home/text.txt')) #it wil print thr base name i ffile exits or not 
print(os.path.dirname('/Home/text.txt'))
print(os.path.split('/Home/text.txt'))
print(os.path.splitext('/Home/text.txt')) # spiting the text with the file text and extension
print(os.path.exists('/Home/text.txt'))
print(os.path.isdir('/Home/jp/'))
print(os.path.isfile('/Home/text.txt'))

print(dir(os.path))
