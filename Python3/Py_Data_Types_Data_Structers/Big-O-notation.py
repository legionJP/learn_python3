'''O(1)
You use a constant time algorithm that takes O(1) (O-of-one) time to
compute. This determines that it will only take one computation to complete a task.
An example of this is to print an item from an array. '''
# An array with 5 numbers 
array = [0,1,2,3,4]

# retrieve the number found at index location 3 
print(array[3]) 


'''O(n)
an example of O(n). Taking the same array, an if statement is written that looks for the number 5. 
To establish that 5 is not there, it has to check every item in the array. '''

# an array with 10 numbers , here 10 checks must be made befor the programs ends.
array = [0,1,2,3,4,6,7,8,9,10]

if 5 in array:
    print("five is still alive")


'''O(log(n))
This search is less intensive than O(n) but more work than O(1).
O(log n) is a logarithmic search and it will increase as new inputs are added but 
these inputs only offer marginal increases.
An excellent example of this in action is a binary search.
 
This solution would have a time complexity of O(log n).
Even if n (the range of numbers entered) is ten times bigger. 
It will not take ten times as many guesses.'''

array = [0,1,2,3,4,6,7,8,9,10]
print("Step one- 'Array' ")
midpoint =int(len(array)/2)
print("the midpoint at step one is :", array[midpoint])

print('Step two')
array= array[:midpoint]  #items before the 6 
print('array', array)
midpoint=int(len(array)/2)
print("the midpoint is: ",  array[midpoint])

print()
print("##Step Three") 
array = array[midpoint:] # so the array is halved at the midpoint
print(array)
# check for the midpoint 
midpoint=int(len(array)/2)
print("the midpoint is: " ,array[midpoint])
# is 4 < 5 
# yes look to the right

print()
print("##Step Four") 
print(array[midpoint:]) 
# check for the midpoint 
array = array[midpoint:] # so the array is halved at the midpoint
midpoint=int(len(array)/2)

print()

print()
print("##Step Five") 
array = array[midpoint:] 
print(array)
print("only one value to check and it is not 5")

'''
we can see that it is not O(1) because the answer is not immediate. 
It is not big-O(n) because the number of guesses does not go up with the size n of the array.
 So here, one says that the complexity is O(log(n)).'''


'''look at a log table up to 100,000,000. This lens shows that O(log n) incurs only a minimal processing cost. Running a binary search on an array with any n values will,
in a worst-case scenario, always make the 
number of computations found in the log values column. '''



'''
O(n^2)
******

O(n^2) is heavy on computation.
 This is quadratic complexity, 
 meaning that the work is doubled for every element in the array. '''

new_array=[] # array to hold the resulted  values
array=[0,1,2,3,4]
for i in range(len(array)): # array fo five values , so this n=5
    for j in range(len(array)): # array of five values , so n=5
        new_array.append(i*j) 
print(len(new_array)) # now the array is doubled size
n=5
print(n*n)


#how many computations does my solution employ and is there a better way?"
