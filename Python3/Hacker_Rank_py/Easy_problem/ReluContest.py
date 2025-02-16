# Enter your code here. Read input from STDIN. Print output to STDOUT
def generate_strings(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            result.append("QuadHex")
        elif i % 4 == 0:
            result.append("Quad")
        elif i % 6 == 0:
            result.append("Hex")
        else:
            result.append(str(i))
    
    return f'[{",".join(f"\"{item}\"" for item in result)}]'

n = int(input())
output = generate_strings(n)
print(output) 


# Question 2 : 
import re

def valid_vehicle_number(s):
    pattern = r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}'
    
    if re.search(pattern, s):
        return True
    else:
        return False

# Input
s = input().strip()
print(valid_vehicle_number(s))



# Question 3 : 

from collections import deque

def canCross(tiles):
    reachable = set(tiles)
    queue = deque([(0, 1)])
    visited = set([(0, 1)])

    while queue:
        current_tile, last_jump = queue.popleft()
        if current_tile == tiles[-1]:
            return True
        for jump in (last_jump - 1, last_jump, last_jump + 1):
            if jump > 0 and current_tile + jump in reachable and (current_tile + jump, jump) not in visited:
                visited.add((current_tile + jump, jump))
                queue.append((current_tile + jump, jump))

    return False

tiles = list(map(int,input().split()))
print(canCross(tiles))