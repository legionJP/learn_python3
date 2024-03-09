'''There are two functions for the file handling
    1). File Opening: Used for the reading , Writting , Creating 
    2). File Closing


Open file accept two arguments:

1). open(file_name file_location, mode)
: 2n argument mode indicates what action is required reading , writting or creating
: Output format : also specifies if you want a output in the form of the text or binary


Modes of File handling in the python

Modes Sets

1). Mode = 'r'
r: it is used to open and read a file in a text format 

2).Mode 'rb'
it used to read and open the file in a binary format 

3).Mode "r+"

it is used for open a file for both  read and write 

4).Mode = 'w'
it is used to opemn a file for writting , but it will overwrite exixting file 

 5). Mode = 'a'

it is used for open files and  editing or  appending the data 
open(<file_name> ,a)   : "it  start write operation at  the end of the file" 

6). close()
it is the function for closing the open file connection and didn't take any arguements

One more way to open the file and no need to close the file 

7). with open('texting.txt',r) as file:

Note: for binary format in every mode add the 'b' in the last 

'''
'''
file=open('text1.txt',mode='r')  # it opens the file from the current directory 
data=file.readline()
print(data)
file.close()
print(file.mode)
'''
#------------------------------------------------------------------------------------

#using of the with open 

with open('text1.txt',mode='r+') as file: #file is the variable name , this method auto close the file 
    data= file.readline()
    print(data)
print(file.closed) #returns true
#----------------------------------------------------------------------------------

from pathlib import Path
file_path= Path(r"d:\\JP Data E\\Notes_BIA_Course\\note_Information_Tech.txt")
try:
    with open('file_path',mode='r') as read_file:
     data=read_file.readline()
     print(data)
except Exception : NotADirectoryError 
print("file not found")  # how to read and write the file from the other  dirctories 

with open('text1.text', mode= 'w') as write_file:
    write_file.write("Hello, This is Me ")
with open('text1.text', mode='r') as read_file:
    data=read_file.readline()
    print(data)  
with open('text1.text', mode='a') as append_file:
    append_file.write(' and who are you')
with open('text1.text',mode='r') as read_file:
    print(read_file.read())         


#without the with open file functions:
file=open('text1.text',mode='r')
data=file.readline
print(data)
file.close()