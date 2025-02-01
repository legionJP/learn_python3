# __a__=10
# _a = 20
# a_ = 30

# print(__a__)


def swap_case(s):
    swap_list = ""
    for i in s:
        if swap_list.islower()==i:
            swap_list.append(i.lower())
        else:
            swap_list.append(i.upper())         
    return swap_list

s = input()
result = swap_case(s)
print(result)