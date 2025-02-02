
# joining tge String using the slicing 
string = "abracadabra"
new_string = string[:5] + "k" + string[6:]
print(new_string)

# Using the list 
string = "abracadabra"
list_string = list(string)
print(list_string)
list_string[5] = "k"
print(list_string)
string = ''.join(list_string)
print(string)

# Using the replace method
string = "abracadabra"
string = string.replace("a","k",5)
print(string)

# Making the Replace function

def mutate_string(string, position, character):
    string1 = list(string)
    string1[position] =character
    new_string = ''.join(string1)
    return new_string
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)