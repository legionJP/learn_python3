def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y==0:
        raise ValueError("can't divide by zero")
    return x/y
    #return x//y #for flor division
