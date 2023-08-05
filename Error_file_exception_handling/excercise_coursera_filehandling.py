f = open("newfile1", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(f_content)

import random
f = open("newfile1", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
'''
import random 
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()  
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))'''


#for printing the random content from the file as spliting them into list 
import random
f=open('newfile.txt','r')
f_content=f.read()
f_content_list=f_content.split("\n")
print(random.choice(f_content_list))







