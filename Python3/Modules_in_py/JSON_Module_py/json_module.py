import json

people_string = '''
{
"people":[
{
"name": "Johny Bairestow",
"phone": "908-976-4532",
"emails": ["bairjohny@email.com", "johnybair@email.com"],
"license_status": false
},
{
"name": "Buttler",
"phone": "123-122-2345",
"emails": ["buttlerjosh@email.com", "joshbuttler@email.com"],
"license_status": true
}
]
}
'''
#-------------------------------------------------------
# loading this  json string in python as a py object 
#------------------------------------------------------

# json.load method loads a file and the json.loads load a string

data = json.loads(people_string)
print(type(data))

#Json Decoders in python 
'''
JSON         Python

object          dict 
array           list 
string          str
number(int),   (float) int , float  
true            True 
false           False 
null            None
'''

print(data)
print(type(data['people']))

for person in data['people']:
    print(person)
    print(person['name'])

#Dumping the python object from the json string 

    del person['phone']
new_string = json.dumps(data,indent=2, sort_keys= True) #indent method for data formating 
print(new_string)

# Loading the  Json file in python object and back in json file 

import json 

with open('states.json') as file:
    file_data = json.load(file)

for state in file_data['states']: #acces the state key
    #print(state)   
    #print(state['name'], state['abbreviation'])

    #deleting the key 
    del state['area_codes']
    #print(state) 

#json.dump and json.dumps method
    
with open('new_states.json','w') as f:
    json.dump(file_data , f,indent=2)

#------------------------------------------
# Parsing the Json data from the Public API 
#-------------------------------------------
    
import json   
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?fromat=json") as response:
    source = response.read()
print(source)


 