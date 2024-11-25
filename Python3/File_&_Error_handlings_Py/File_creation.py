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

#------------------------------------------------------------------------------------------------#

# Read

file =open('Python3/test.log','r')
print(file)
#print(file.read())
print(file.readline(),end="")  # read one line every time by the iteration or pointer
print(file.readline(4)) # only print the 4 char.

for data in file:
    print(data) #one by one everything is being printed

# Write 

f1 = open('demo','w')
f1.write("This is me writing the unwanted things ") # if only the 2nd statement is executed than 1 is overrided
f1.write("This line 2")

# Append
f1 = open('demo','a')
f1.write("This is me writing the unwanted things ") # if only the 2nd statement is executed than 1 is overrided
f1.write("This line 2")

# using the binary mode to open 
img = open("Python3/image.png",'rb')
# for i in img:
#     print(i)

f1 = open('sample.png','wb') #Copy the img file 
for i in img:
    f1.write(i)


