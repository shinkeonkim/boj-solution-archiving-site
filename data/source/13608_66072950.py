while 1:
    n = int(input())
    
    if n == 0:
        break
    
    l = [[*map(int, input().split())] for i in range(n)]
    
    s = 0
    left = 0
    for i, cnt in l:
        s += cnt // 4
        
        left += (cnt % 4) // 2
        
    s += left // 2
    
    print(s)
