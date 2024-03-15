'''1. Synatx erorr  : misspelling or typo
       Identation error 


Exception handling Error: 

These are occurr during the execution and needs to be handled

Errors are unavoidable in programming and in Python, it is no different, these needs to be handled

developer need to deal with the issue and keep from failing
'''


def divide_fun(a,b):
    return a/b
#print(divide_fun(40,0)) #calling the fun by the print fun and it returns the a/b
try:
    ans= divide_fun(40,0)

except Exception as e:
    print("something went the wrong! " + " ",e)
    print(e.__class__)  #common base class for non exit exceptions 

    #using the base class exception inside the except , 
    #it is used for the all exceptions in the python.
    # you can give the e after the exceptions ,  
    #so E vaariable acts as a alias for the exceptions
    #means e can print hte content of the error message


#or
def divide_by(a,b):
    return a/b
try:
    ans= divide_by(10,0)
except ZeroDivisionError as e:
    print(e, "we cant divide by the zero")
except Exception as e: 
    print(e,"something went worng") 
    
# handle more than one exception by chaining the except statement by adding another except statement. 
#zero divison error
    
# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:

        print(file.read())
except Exception as e:
    print("The file could not be found ")    

# Starter code
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except ZeroDivisionError as e:
    print("Can't divide by the zero:",e)



# also zero divison error
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)

# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except Exception as e:
    print("Item does not exist in the list", e)

####################################################

try:
   f = open('file1.txt')
   #if f.name =='file1.txt':
    #   raise Exception               #Raisning exception manually
except FileNotFoundError  as e:
    print(e)
except Exception as e:  # place general excpetion in the last for  printing if it is  in expect or custum error 
    print('Error')            
else:                    # it runs when there is no exception
    print(f.read())
    f.close()
finally:
    print("Excecuting the finally to see the process")
