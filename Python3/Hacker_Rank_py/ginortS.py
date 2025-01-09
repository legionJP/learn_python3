'''

Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
'''

import re
input_list = str(input())
result_list =""

pattern1 = re.compile(r'[a-z]')
matches = pattern1.findall(input_list)
matches=sorted(matches)
for i in matches:
    result_list+=i

pattern2 = re.compile(r'[A-Z]')
matches2 = pattern2.findall(input_list)
matches2=sorted(matches2)

for i in matches2:
    result_list+=i

pattern3 = re.compile(r'[0-9]')
matches3 = pattern3.findall(input_list)
matches3=sorted(matches3)
for i in matches3:
    if int(i) %2!=0:
        result_list+=i
for i in matches3:
    if int(i) % 2==0:
        result_list+=i
 
print(result_list)


def simpleArraySum(ar):
    # Write your code here
    sum_arr = 0
    for i in ar:
        sum_arr +=i
    return sum_arr
ar1 = [2,3,4,1]
print(simpleArraySum(ar1))

# for s in input_list:
#     if input_list.__contains__():
#         result_list.append(sorted(input_list))
# print(result_list)

# Solution 2
import re
input_list = str(input())
result_list =""

pattern = re.compile(r'[a-zA-Z0-9]')
matches = pattern.findall(input_list)

lower_case= sorted([x for x in matches if x.islower()])
upper_case = sorted([x for x in matches if x.isupper()])
odd_numeric_case = sorted([x for x in matches if x.isnumeric() and int(x)%2!=0])
even_numeric_case = sorted([x for x in matches if x.isnumeric() and int(x)%2==0])

result_list = ''.join(lower_case+upper_case+odd_numeric_case+even_numeric_case)
print(result_list)