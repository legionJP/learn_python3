import re

emails = '''
myWork@gmail.com
my.work@academic.ac
my-121-work@my-office.net       

'''


pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|ac)')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)
for match in matches:
    print(match)

urls = '''
https://www.google.com
https://jps.com
https://youtube.com
https://www.github.com

'''    

pattern = re.compile(r'https?://(www\.)?')  # grouping the 'www' and \. for escaping the 

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') 

# there is three group #1. group for optional www. 
#2. second is for the word charcter for domain name, 3). for the .com domain , 
#group 0 is entire result match than this has the index groups 0,1,2.

#Back Refrencing 

subbed_url = pattern.sub(r'\2\3',urls) # using the pattern to substitude the group 2 and 3 for all matches in the url

matches1 =pattern.finditer(urls)
for match in matches1:
    print(match.group(1))

print(subbed_url)


#Flags 

sentence = 'Start a debat and bring it on the conclusion'
pattern = re.compile(r'start',re.IGNORECASE)

matches = pattern.search(sentence)
print(matches)