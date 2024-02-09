message ="Hello Jp's World"
print(message)

print(len(message))
print(message[2])
print(message[0:6]) 
print(message.count('l'))
print(message.count('World')) # counting the string chracter
#Find the string character 
print(message.find('Jp'))  #the ouput is 6 because the word is strating from the index 6
print(message.find('y'))

#Replacing the String 

message=message.replace('Hello' , 'Welcome')
print(message)

#Cocatinatong the string

greeting = "hello"
name = 'JP'
message = greeting + ',' + name + ' welcome '
print(message)

# String formating 
message= '{}, {} welcome'.format(greeting,name)
print(message)

#fstring fromating
message= f'{greeting}, {name.upper()}.Welcome!'
print(message)

#Find the help about the methods and attributes of the string and funtion 
#in
print(dir(name))
print(help(str))