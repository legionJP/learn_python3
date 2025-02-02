# print(any([1>0,1==0,1<0]))
# print(any([1<0,2<1,3<2]))

# print(all(['a'<'b','b'<'c']))

# print(all(['a'<'b','c'<'b']))

N = int(input())

input_list = list(map(int, input().split()))
if len(input_list) == N and all(x >= 0 for x in input_list) and any(str(x) == str(x)[::-1] for x in input_list) :
    print(True)
else:
    print(False)


# N = int(input())
# input_list = list(map(int,input().split()))
# print(len(input_list)==N and all(x>=0 for x in input_list) and any(str(x)==str(x)[::-1] for x in input_list))
    
        
    
