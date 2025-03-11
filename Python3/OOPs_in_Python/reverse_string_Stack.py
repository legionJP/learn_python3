
# stack
from collections import deque
#stack =deque()

class Stack():
   def __init__(self) -> None:
      self.stack=deque()

   def push(self,item):
      self.stack.append(item)

   def pop(self):      
      return self.stack.pop()
   
   def is_empty(self):
      return len(self.stack) ==0

string ="gninrael nIdekniL htiw tol a nraeL "
reversed_string = ""

stack=Stack()

for char in string:
  stack.push(char)
while not stack.is_empty():
    reversed_string += stack.pop()

print(reversed_string)