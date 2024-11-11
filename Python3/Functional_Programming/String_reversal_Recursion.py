''' 
String Reversal using slice function

str=str[start:stop:step]
'''
string_1 = "Legion"
new_stirng =string_1[::-1]
print(new_stirng)

#function for the revese string

def string_reversal(str):
    if len(str) ==0:
        return str
    else:
        return string_reversal(str[1:])+ str[0] # : after slice mark the string or number will be included 
    
str = str(input("type the string for rversal "))
reversal=(string_reversal(str))
print('reverse string  of {} is {}' .format(str,reversal))
