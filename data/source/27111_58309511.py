d = {}

ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    
    if b == 0:
        # 나왔다.
        
        if a in d and d[a] == 0:
            # 또 나간 기록이라면 누락
            ans += 1
        elif a not in d:
            # 기록이 없다.
            ans += 1
        
    elif b == 1:
        # 들어갔다.
        
        if a in d and d[a] == 1:
            # 또 들어온 기록이라면 누락
            ans += 1

    d[a] = b

ans += [*d.values()].count(1)
    
print(ans)
