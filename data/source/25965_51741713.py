for _ in range(int(input())):
    ans = 0
    
    l = [[*map(int,input().split())] for i in range(int(input()))]
    k, d, a = map(int,input().split())
    
    for kk, dd, aa in l:
        t = kk * k - dd * d + aa * a
        
        if t < 0:
            continue
        
        ans += t
    
    print(ans)
