#for loop condition 

for i in range(10):
    print('loop----',i)
for i in range(1,10): # it will not include the 10
    print(i)
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

# nested loop with the string iterations

for num in nums:
    for letter in 'abc':
        print(num,letter)


#****************************************************************************************************************

#While loop condition 

x=0
while x<10:
#while True:
    if x==5:
        break    
    print(x)
    x+= 1


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
#when we need a particular item in the list then use of the if condition and after founding the required item ,there is no need of continuing of the loop 
favorites1= ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for dessert in favorites1:
    if dessert=='Apple pie':
        print('fav dessert is',dessert)
        break 

#if the required item is not found in the list than we have to handle the exception
    else:
        print('the dessert is not on my list ')


#if the required item is in the list then we have to use the break to handle the else part
#          
#continue
#use of the continue is the similar to control the iteration of the loop 
#,by using the continue it skip the that section of the loop and
#continue with the rest.
        
favorites=['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for desseret in favorites:
    if desseret=='Apple pie':
        continue 
        print('fav desssert is ',desseret)

 #Pass condition is used and allow us to completely ignore that if condition is satisfied or not
 #Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == ' Rasgulla':
        pass
    print('Other desserts I like are', dessert) 
