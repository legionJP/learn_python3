# Duck typing and Easier to ask forgiveness than permission(EAFP)
# Duck typing means object walk like duck and quacks like duck means what types of object it is it should what is ask to do 


class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Person:
    def quack(self):
        print('I am Quacking like a duck')

    def fly(self):
        print('I\'m Flapping my Arms!')                

def quack_and_fly(thing):
    #Not duck type Non pythonic

    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()

    else: 
        print('This has to be duck!')
    print()

    

    
