#---------------------------------------------------------------------------------------------#
#                                  File Readings:
#---------------------------------------------------------------------------------------------#
 
'''
2). file.readlines(): 
____________________
The Readlines method reads the entire contents of the file and then returns it in an ordered list.

This is useful because it allows you to iterate over the list or pick out specific lines based on a condition.
****************************************
1). file.read(): 
___________
The Read method returns the entire contents of the file as a string that will contain all the characters.
 
file.read(40): passing the integer to return the specified number of the charachter 

3). readline()
_____________
it return a single line as a striing 

readline(n)
 it also can return thhe number of the specified character on a single line 

'''


''' When Working with the differnt Directories:
Absolute __path__
_________________:  It  contain all the information of the driver and the file  with the leading '/' slash mark
 C:\\user\\system\\file.txt
 /user/local/etc/file1.txt
Realative __path
________________ : it didnt contain any info about the root file and contain info of the file in current working directory'''

with open('newfile.txt', 'r') as file:
    print(file.read())
#for reading the charcter in the as given limit 
    print(file.read(10))   
# for reading hte only one line 
with open('newfile1','r') as file:
    print(file.readline())


# for reading the multiple lines which accepts the list format so we can assign the varriable and can put the loop
#for printing the list item line by line 

with open('newfile1','r') as file:
    data= file.readlines()
for i in data:
    print(i)    

'''# or you cn use the 
with open('newfile1','r') as file:
    for i in data:
       print(i)    
'''