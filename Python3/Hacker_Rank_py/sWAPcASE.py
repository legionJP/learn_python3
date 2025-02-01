# __a__=10
# _a = 20
# a_ = 30

# print(__a__)

def swap_case(s):
    result=""
    for i in s:
        if  i.islower():
            result+=i.upper()
        else: 
            result+=i.lower()
    return result
        
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)