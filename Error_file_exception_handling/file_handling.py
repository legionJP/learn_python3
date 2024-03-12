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

file=open('text1.txt',mode='r')  # it opens the file from the current directory 
data=file.readline()
#data =file.read(120) #it will be read the 120 charcter than returns empty string
print(data,end='')
file.close()
print(file.mode)

#------------------------------------------------------------------------------------

#using of the with open 

with open('text1.txt',mode='r+') as file: #file is the variable name , this method auto close the file 
    data= file.readline()
    print(data)
#print(data,end='')
print(file.closed) #returns true
#----------------------------------------------------------------------------------
'''
for line in file:
    print(line,end='')


#using the while loop
    
size_to_readd =20
f_data=file.read(size_to_readd)

while  len(f_data)>20:
    print(f_data,end='')
    f_data=file.read(size_to_readd)

'''
#-------------------------------------------------
#Writing the file
with open('text2.txt','w') as f:
    #pass
    f.write('Test')
    f.seek(0) # It will overwrite the first operation 
    f.write('T')

#------------------------------------------------------
    
with open ('text1.txt','r') as read_file:
    with open('text_copy','w') as write_file:
     for line in read_file:
        write_file.write(line)
        # also can be copy images as a 'rb' mode and 'wb'

# Example

with open ('image.png','rb') as rf:
   with open ('copy_image.png','wb') as wf:
      file_size = 15173
      rf_file_size =rf.read(file_size)
      while len(rf_file_size) > 0:
         wf.write(rf_file_size)
         rf_file_size =rf.read(file_size)


#---------------------------------------------------
#Opening th file from the given path 

from pathlib import Path
file_path= Path(r"d:\\JP Data E\\Notes_BIA_Course\\note_Information_Tech.txt")
try:
    with open('file_path',mode='r') as read_file:
     data=read_file.readline()
     print(data)
except Exception : NotADirectoryError 
print("file not found")  # how to read and write the file from the other  dirctories 

#---------------------------------------------------------

#'w' 'r' , 'a' operation on the file


with open('text1.text', mode= 'w') as write_file:
    write_file.write("Hello, This is Me ")

with open('text1.text', mode='r') as read_file:
    data=read_file.readline()
    print(data)  

with open('text1.text', mode='a') as append_file:
    append_file.write(' and who are you')

with open('text1.text',mode='r') as read_file:
    print(read_file.read())         

#---------------------------------------------------------------------------

#without the with open file functions:
file=open('text1.text',mode='r')
data=file.readline
print(data)
file.close()
