from typing import List
def swapN(a:list, b:list) -> None:
    a[0],b[0] =b[0],a[0]
    print(a[0],b[0])

a,b= map(int,input().split())
a_1,b_1= [a],[b]
swapN(a_1,b_1) 