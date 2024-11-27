import re

# .finditer   it returns extra options with all functionality
# .findall() it just returns the matches as a list of string


text_to_search = ''' abcdefghijklmnopqrstuvxyz

ABCDEFGHIJKLMNOPQRSTUVWXYZ
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

Mr. Jps
Ms Dubi
Mrs. Xinp
Mr Thei


###################################################################
# Character matches in compile regex

. - Any Character except New line ()'\')  (. - period sign )
\d -Digit (0-9)
\D - Not a digit (0-9)
\w Word Charcter (a-z, A-Z, 0-9, _)
\W - Not a word character
\s - White space (space, tab ,newline)
\S - Not white space(space, tab ,newline)

(Note: \. called the literal )
# Anchers

\b - Word boundary 
\B - Not a word boundary 
^ - Beginnig of a string 
$ - Enof string 
[] - Matches Characters in brackets (name: Character Set)

[^ ] - Matches characters Not in

|  -Either or 
( ) -Group

# Quantifiers:

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

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # Matching the exact numbers

pattern = re.compile(r'Mr\.')
pattern = re.compile(r'Mr\.?\s[A-z]') #Question  Mark for matching of 0 or 1 either

pattern = re.compile(r'Mr\.?\s[A-z]\w*') # word character

pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-z]\w*') # Usinga group  pattern within 

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # for printing the .findall()
#pattern = re.compile(r'\.') #literal search
#pattern = re.compile(r'legion\.com')


matches = pattern.findall(text_to_search) 
matches = pattern.finditer(text_to_search) #(method) def finditer(strin)


'''
pattern = re.compile(r'Start')
matches = pattern.match(sentence) 
matches = pattern.search(sentence) # returns all the matches at any plaace in string

print(sentence)
'''

for match2 in matches:
    print(match2)

#print(text_to_search[1:4])


#parsing the data from the file 
    
with open ('text2.txt','r') as f:
    contents =f.read()
    matches1= pattern.finditer(contents)


    for match1 in matches1:
        print(match1)
