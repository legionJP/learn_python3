str = "Hello what are you"

def char_count(input_str):
    char_dict = {}
    str1 = input_str.lower()
    for char in str1:
        # skip the space
        if char == " ":
            continue
        if char in char_dict:
            char_dict[char]+=1
        else: 
            char_dict[char] =1
    return char_dict    

result = char_count(str)

for char, count in result.items():
    print(f"{char}: {count}")

