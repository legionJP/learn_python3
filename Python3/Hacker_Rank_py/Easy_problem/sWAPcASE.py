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

# Using the list comprehension
def swap_case(s):
    return ''.join([ i.upper() if i.islower() else i.lower() for i in s])

# return ''.join(
#     [i.upper() for i in s if i.islower()] +
#     [i.lower() for i in s if not i.islower()]
# )
# [expression for item in iterable if condition]
# result = [i.upper() for i in s if i.islower()] + [i.lower() for i in s if i.isupper()]
# final_result = ''.join(result)

        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)