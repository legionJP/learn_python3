
# stack
from collections import deque
stack =deque()
class Stack():
    string ="gninrael nIdekniL htiw tol a nraeL "
    reversed_string = " "
 

    for char in string:
     stack.push(char)
     while not stack.is_empty():
       reversed_string += stack.pop()

    print(reversed_string)      