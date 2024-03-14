import re

text_to_search = ''' abcdefghijklmnopqrstuvxyz

BCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Yeah YeahYeah

#if Word has the space then it is a word boundary string

MetaCharcters (Need to be escaped):

. ^ $ * + { } [ ] \ | ( )

legion.com

123-444-5678
321.555.0987

800-123-1234
900-123-5678

321*123*1235

MR JSP
Mr You 
Mr They

# Character matches in compile regex

. - Any Character except New line ()'\')
\d -Digit (0-9)
\D - Not a digit (0-9)
\w Word Charcter (a-z, A-Z, 0-9, _)
\W - Not a word character
\s - White space (space, tab ,newline)
\S - Not white space(space, tab ,newline)

# Anchers

\b - Word boundary 
\B - Not a word boundary 
^ - Beginnig of a string 
$ - Enof string 
[] - Matches Characters in brackets (name: Character Set)

[^ ] - Matches characters Not in

|  -Either or 
( ) -Group

Quantifiers:

* - match 0 or more
+ - 1 0r more
? - 0 or One
{3} - Exact Numbers in count
{3,4} - Range of Numbers(Min, Max)


#################################################################################

Pat
Sat
bat 
Mat


'''
#Row string

print('\tTab')
print(r'\tTab')  # r is for row string 

sentence = 'Start a debat and bring it on the conclusion'

#compile Method

pattern = re.compile(r'abc') #Compile a regular expression pattern, returning a Pattern object.

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # it matches the pattern which was required
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')   

#(Matching the 800, 900 , with the character set and putting literal) 
'''when '-' is put in the character set at the begning or last it will match just - literal character
but in the between file it will specify the range'''

pattern = re.compile(r'[a-zA-Z]') # or just [a-z]
pattern = re.compile(r'[^b]at') # not a b with the at character

pattern = re.compile(r'\d{3}.\d\d\d.\d\d\d\d') 
#pattern = re.compile(r'\.') #literal search
#pattern = re.compile(r'legion\.com')


matches = pattern.finditer(text_to_search) #(method) def finditer(strin)
#matches = pattern.finditer(sentence)

for match in matches:
    print(match)

#print(text_to_search[1:4])


#parsing the data from the file 
    
with open ('text2.txt','r') as f:
    contents =f.read()
    matches1= pattern.finditer(contents)

    for match in matches1:
        print(match)
