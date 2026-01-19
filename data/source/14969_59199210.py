while 1:
    n, m = map(int, input().split())
    
    if n == 0:
        break
    l = [*map(int, input().split())]
    
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            s = l[i] + l[j]
            
            if s > m:
                continue
            ans = max(ans, l[i] + l[j])
    print(ans if ans > 0 else "NONE")
