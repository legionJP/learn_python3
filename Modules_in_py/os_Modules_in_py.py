

'''The OS module provides us a layer of abstraction between us and
the operating system. When we are working with os module always 
specify the absolute path depending upon the operating system 
the code can run on any os but we need to change the path exactly. 
If you try to 
remove a file that does not exist you will get FileNotFoundError'''

import os
print(dir(os))
cwd=os.getcwd()
print(os.getcwd())
print("current working directory is",cwd)


#Chnage the curent working directory 

print("current working directory  before is",cwd)
changedir=os.chdir('C:/Users/jjpsi/Py_Notes/')

print("the new working directory is ", changedir)
print(os.getcwd())

print(os.listdir()) # geeting the list of directiories in the current path


#Creating a directory
#os.mkdir('../')    # used to create a directory named path with the specified numeric mode. This method raises
#FileExistsError if the directory to be created already exists.
directory ='jppal' #to be created
parent_dir='/home/..'
path = os.path.join(parent_dir,directory)
#os.mkdir(path)
print("directory '%s' created " % directory)


#os.makedirs(path)  #Super-mkdir; create a leaf directory and 
'''all intermediate ones. Works like mkdir, except that
any intermediate path segment (not just the rightmost) will be created 
if it does not exist. If the target directory already exists, 
raise an OSError if exist_ok is False. 
Otherwise no exception is raised. This is recursive'''
print("directory '%s' created " % directory)

'''#Specified numeric Mode

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
#os.makedirs(path)
os.listdir()

#os.listdir
path = '/'
dir_list = os.listdir(path)
print("files and direcotries in ' ", path,"' :")
print(dir_list)

'''os.remove('/')
os.rmdir('/') #to remove the empty directory
os.remove(path)
os.rmdir(path)'''

os.name
print(os.name)
#This function gives the name of the operating system dependent module imported. The following names have currently been registered:
#‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’
os. error
#IO error

os.popen

file = os.popen('fd', 'w')
file.write("Hello")
os.close

#os.remove('filename')

file = os.popen('fd,' 'w')
file.write("Hello")
os.close(file)

os.rename('fd','new.txt')


os.path.exists("file_nmae")
os.path.getsize('file_name') #prints in the bytes
result = os.path.exists("file_name") #giving the name of the file as a parameter.
  
print(result) #true or false 


