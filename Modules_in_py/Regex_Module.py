import re

text_to_search = ''' abcdefghijklmnopqrstuvxyz

BCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Yeah Yeah 

MetaCharcters (Need to be escaped):
. ^ $ * + { } [ ] \ | ( )

legion.com

243214-12323-3232
232134-3244-32432
MR JSP
Mr You 
Mr They

'''
#Row string

print('\tTab')
print(r'\tTab')  # r is for row string 
sentence = 'Start a debat and bring it on the conclusion'

#compile Method

pattern = re.compile(r'abc') #Compile a regular expression pattern, returning a Pattern object.
#pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search) #(method) def finditer(strin)

for match in matches:
    print(match)
print(text_to_search[1:4])
