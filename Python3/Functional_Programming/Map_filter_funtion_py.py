#Using the map function
menu=['India','USA','Rusia','Africa','Bharat']

def find_in_map(country):

    if country[0] == 'I':

        return country
    
map_country=map(find_in_map,menu) # first argu ment is function itself then the iterable item/     
print(map_country)                             #and here functions is not calling but using to give argument not 
for x in map_country:
    print(x)


#Using the Filter Function

menu1=['asia', 'australia','North America','Antartica']

def find_in_world(continent):
    if continent[0]=='a':
        return continent
filetr_in_world=filter(find_in_world,menu1)
print(filetr_in_world)
for x in filetr_in_world:

   print(x)    


#Note:  Map() returns every item in an iterable 
# and filter() returns  all item  when functions returns   True.