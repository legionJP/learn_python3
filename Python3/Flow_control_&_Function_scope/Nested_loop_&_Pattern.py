#---------------------------- Pattern Printing -----------------------------------------#
#---------------------------------------------------------------------------------------#
#1.
for f in range(4):            # Here f is printing the number of the rows and his columns
    for h in range(4): #0 to 3
        print("# ", end="")
    print() # print new line
print('-----------------')
#-----------------------------------------------------------------------------#
#2. 
for i in range(4):   
    for h in range(4-i):  
        print("# ", end="")
    #h+=1
    print()    
#---------------------------------------------------------------------------------------#
# Pattern : # 1 2 3 4     2.    A P Q R
#             2 3 4             A B Q R
#             3 4               A B C R
#             4                 A B C D

#--------------------------------------------------------------------------------#
#nested For Loop
  #1. Outer loop

     #2.Inner Loop

list1 =[1,2,3,4,5,6,7,8,9]

list2 =[1,2,3,4,5,6,7,8,9]
count=0
#outer_loop
for x in list1:
    count+=1
    #inner loop
    for y in list2:
        count+=1
print(count)        

#outer loop
for i in range(10):
    #innner loop
    for j in range(10):
        print(0,end =" ")
    print()   #separating the line

import time
start_time=time.time()

# #outer loop
# for i in range(10):
#     #inner loop
#     for j in range(100):
#         print(0, end=" ")
# print()        
# print(round((time.time()-start_time),2))
# # so we have to optimizee our code to run efficiently and effectively


# #Enumearte function 
# # finding the number in a list with the help of the enumerate function 
# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# for x,num in enumerate(num_list):
#     if num == 36:
#         print('Number found at ', x)

#--------------------------------------------------------------------------------#