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

#Json Deoders in python 
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

#-----------------------------------------------------
# Loading the  Json file in python object and back in json file 
#---------------------------------------------------------

import json 

with open('states.json') as file:
    file_data = json.load(file)

for state in file_data['states']: #acces the state key
    #print(state)   
    #print(state['name'], state['abbreviation'])

    #deleting the key 
    del state['area_codes']
    #print(state) 

    
#---------------------------------------
#json.dump and json.dumps method
#---------------------------------------    
with open('new_states.json','w') as f:
    json.dump(file_data , f,indent=2)

#------------------------------------------
# Parsing the Json data from the Public API 
#-------------------------------------------
    
import json   
import requests
import urllib.request
from urllib.request import urlopen

with  requests.get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey=6dc0c80fdc874a7d8bd3136da9d18dfc")as response:
    source = response.json()
#print(source)

# with open ('response2.json', 'w') as currency_data:
#      json.dump(source,currency_data, indent=2)

with open('response2.json') as currency_exchange:
    currency_data1 = json.load(currency_exchange)
print(currency_data1)
print(len(currency_data1))

#------------------------------------------------------
# If the response is the list than coverting the currency value
#-----------------------------------------------------

usd_rates = dict()
for item in currency_data1['rates']['base']:
    print(item)
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price
    print(name, price)

print(50* float(usd_rates['USD/EUR']))

#-----------------------------------------------------

# resp = requests.get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey=6dc0c80fdc874a7d8bd3136da9d18dfc")
# print(resp.json())
# print(type(resp))

# for item in resp['rates']:
#     print(item)


# import http.client

# conn = http.client.HTTPSConnection("api.currencyfreaks.com")
# payload = ''
# headers = {}
# conn.request("GET", "/v2.0/convert/latest?from=usd&to=pkr&amount=500&apikey=6dc0c80fdc874a7d8bd3136da9d18dfc", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))




