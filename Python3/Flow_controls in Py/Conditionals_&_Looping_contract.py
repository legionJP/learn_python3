#--------------------------------------------------------------------------------#
#   If, Elif, Else Statement
#---------------------------------------------------------------------------------#
if True:     # if is the block or suite where the multi statement can be write under this block
    print("this is right") # in the case of the block indentation  use the tab( which is equal to 4 space)
    print('Ok')

#x= 8
x= int(input("enter the num to check odd even"))
r = x%2
if r==0:
    print('even')
    if x > 7:
        print('Reason')
    else:
        print('No Reason')    
else:
    print('Odd')   
# 2 elif
f= 3
if x== 1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Thrid")       
else:
    print("Out of leauge")  
#-----------------------------------------------------------------------------------#       
# positive number 
#-----------------------------------------------------------------------------------#
x= int(input("Enter the number"))
if x>=0:
    print("Positive number")
elif x==0:
    print("it is 0")
else:
    print("Number is negative")  
#-------------------------------------------------------------------------------------------------------#       
# find gratest value12
#-----------------------------------------------------------------------------------------------------------#
x,y,z = map(int,input("Enter the 3 values:").split())   
if x>y and x>z:
    # if x>z:
    print("the greatest is",x)
elif y>z:
    print("the greatest is",y)
else:
    print("the greatest is",z)

# xyz= [x,y,z]
# for i in xyz:
#     if x > y and z & 

#--------------------------------------------------------------------------------#
#                       For loop: For loop works with sequence 
#---------------------------------------------------------------------------------#
l1= ['jp',62,2.5]
for i in l1:
    print(i)

#---------------------------------For loop operation with the range -----------------------------#
for i in range(10):
    print('loop-',i)
for i in range(1,11): # it will not include the 11
    print(i)
for i in range(1,11,2):
    print(i)   
for i in range(22,2,-1): # for descending order bcz range always works in ascending
    print(i)

for i in range(1,20):
    if i%5!=0: #skip the multiple of 5
        print(i) 
#-------------------------------------------------------------------------------------------------------#
fav=['one','two','three']  
for item in fav:
    print('fav',item) 

# 2 Condtion : Iteration of the loop and use of break and continue
    
nums =[1,3,5,7,9]
for num in nums:
    if num==5:
        print('found!')
        #break
        continue
    print(num)
#--------------------------------------------------------------------------------------------------------#
# nested loop with the string iterations

for num in nums:
    for letter in 'abc':
        print(num,letter)

# -----------------------------------------------------------------------------------#
#                             For - Else
# -----------------------------------------------------------------------------------#
num = [10,34,56,55,24,25]
for n in num:
    if n%5==0:
        print(n)
        break # it will print only the 10 as it is first
#2.
num = [10,34,56,55,24,25]
for n in num:
    if n%5==0:
        print(n)
        break # it will print only the 10 as it is first
else:
    print("Not found") # it will break the upper loop if the inner codition is breaked
    #for even first iteration  write the else for for


#****************************************************************************************************************
#                                       While loop condition 
#****************************************************************************************************************

i=1 # i=5
while i <=5: #i>=1
    print('study',i)
    i =i+1 #i =i-1
#------------------------------------#
i= 5
while i>=1:
    print("Outside ", end="") # it will end the new line, end = ""
    j=1    # every time reset the value of j
    while j<=4:
        print("Inner 4time ", end="")
        j =j+1
    i = i-1
# -----------------------------------#    
x=0
while x<10:
#while True:
    if x==5:
        break    
    print(x)
    x+= 1

#-----------------------------------------------------------------------------------------------------------------------#    

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1
    #here the count varriable is used for the comparing the lenght of the varriable
    # for this while loop will work according the count if count is 1 then while will continue after
    # the increment of the 1 
 
#*************************************************************************************************************

#Control flow and the loops...
     
# we have to examine how to use the control and flow of the loop  and exit out when the specific condition is met.
#we also have to use the break, pass and continue...

#If- else for the loop 
#when we need a particular item in the list then use of the if condition and after founding the required item ,
#there is no need of continuing of the loop 
#-----------------------------------------------------------------------------------------------------#
#                                 Breake , Continue and Pass
#-----------------------------------------------------------------------------------------------------#

#1. Breake
#------------

favorites1= ['Creame Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for dessert in favorites1:
    if dessert=='Apple pie':
        print('fav dessert is',dessert)
        break 
#if the required item is not found in the list than we have to handle the exception
    else:
        print('the dessert is not on my list ')

#if the required item is in the list then we have to use the break to handle the else part
#2.
my_list = [1,2,3,4,5]
for i in my_list:
    print(i)

    #if i ==3:
    if i ==6:
        break  #if no break then hits the else statement
else :
    print('Hit the else statement ')    

#3.
def find_index(to_search,target):
    for i in enumerate(to_search): #i, value
        if i == target:   #value == target
            break
        else:
            return -1
        return i 
my_slist= ['JP','AK','VJ']
index_location = find_index(my_slist,'VJ')
print(' Location of target is index: {}'.format(index_location)) 
#-------------------------------------------------------------------------
#4. 
avail = 10
x  = int(input("How many candies you want: "))
i=1
while i <=x:
    if i>=avail:
        print("It is ran out of stock")
        break
    print("candy",i)
    i+=1
print("thanks")

#----------------------------------------------------------------------------

#------------------------------------------------------------------------        
#              continue
#------------------------------------------------------------------------
#use of the continue is the similar to control the iteration of the loop 
#,by using the continue it skip the that section of iteration in  the loop and
#continue with the rest.

 #1.       
favorites=['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for desseret in favorites:
    if desseret=='Apple pie':
        continue 
    print('fav desssert is ',desseret)

# 2.
for i in range(1,500):
    if i%5==0:
        continue # It will just skip the multiple of 5 and continu
    print(i)


 #---------------
 # Pass
 #-------------
 #the pass condition is used and allow us to completely ignore that if condition is satisfied or not
 #Starter Code

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == ' Rasgulla':
        pass
    print('Other desserts I like are', dessert) 

for i in range(1,101):
    if(i%2!=0):
        pass #continue 
    else:
        print(i)
#----------------------------------------------------------------------#
#   Difference Between Breake and Continue and Pass
#----------------------------------------------------------------------

for i in range(5):
    if i ==3:
        continue # skip that iteration
        #break  # it will not print after 3 is met 
        #pass  # to pass the block of class or condition when we have to use it later or we hae to skip it
             
    print(i)
