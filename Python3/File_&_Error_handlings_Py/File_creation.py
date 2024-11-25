#------------------------------------------------------------------------------------------------#
#                  File Creating in py 
#------------------------------------------------------------------------------------------------#

''' 
To write multiple lines of content you use the writelines() function.
You use the write() function to add one line of content and the open() function 
to create, write or read a file.
'''  

with open('newfile.txt', 'w') as write_file:
    data = write_file.write("New file strats from here")
    print(data)

'''for writting the multiple line text 

the function is file.writelines , it accepts the list'''

with open('newfile1','w') as write_file:
    data = write_file.writelines(["New files line 1", "\n New files line 2", "\n New file Line3"])
file=open('newfile1','r')
data=file.read()
print(data)    
file.close()

# use of the Append 

with open('newfile1','a') as write_file:
    data = write_file.writelines(["\nNew files line 1", "\n New files line 2", "\n New file Line3"])
    print(data)
file=open('newfile1','r')
data=file.read()
print(data)
file.close()
