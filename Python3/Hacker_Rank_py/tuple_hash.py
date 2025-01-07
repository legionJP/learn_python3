if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t =()
    for _ in range(n):
        for key , value in integer_list.items():
            t.add(value)
              
        
    print(hash(t))