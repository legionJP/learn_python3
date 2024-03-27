class Stack:
    def __init__(self) -> None:
        self.item =[]   #empty lst              # creting object 

    def is_empty(self):
        #return len(self.item)==0
        return not self.item  
    #inside the class functions are the methods 
    
    def push(self,items):
        self.item.append(items)

    def pop(self):
        return self.item.pop() #return and remove the item defualt at last or from the right as lifo
    
    def peek(self):
        return self.item[-1]
    
    def  size(self):
        return len(self.item)
    
    def __str__(self) -> str:
        return str(self.item)
    
if __name__ == "__main__":
    s= Stack() 
     
''' print(s)

    print(s.is_empty())
    s.push(3)
    s.push("Hello")
    s.push(4)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s.size())   
'''    
string ="gninrael nIdekniL htiw tol a nraeL "
reversed_string=""

#reversing the string using stack
for char in string:
    s.push(char)
while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)      

 