# Named tuples are like a light weight objects thats works just as regular tuples but its more readable

color =(55,155,255)
print(color[0])

#reading the color value/type  by dictionary 

color = {'red': 55, 'Blue': 155, 'Orange': 255}
print(color['red'])

#Using the Namedtuple

from collections import namedtuple

color = namedtuple('color',['red','green', 'Blue']) #typename : color , fieldnames : red,...
color = color(55,155,255)
#color = color(red=55,green=155,Blue= 255)

#print(color['red']) # by using the regular tuple 
print(color.red)  # this is more readdbale form 