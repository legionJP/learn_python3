list_1= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#       -10,-9,-8,-7,-6,-5,-4,-3,,-2,-1

#list[start:end:step]

print (list_1[-1])

print(list_1[0:6])  #end index is not inclusive

print(list_1[-7:-1])
print(list_1[1:-3])

print(list_1[:9]) #this will include the start index
print(list_1[5:]) #this will include the end index

print(list_1[2:-1:2]) # :2 is the step so the list will jump to 2 step of the index
print(list_1[-1:2:-1])
print(list_1[::-1]) # : start , : end then entire reverse list


#Slicing the string

sample_url = 'https://jppal.com'
print(sample_url)
print(sample_url[::-1])
print((sample_url[-4:1]))
prnt((sample_url[7:1]))
