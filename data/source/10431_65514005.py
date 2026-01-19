p = int(input())
for _ in range(p):
    t, *l = [*map(int, input().split())]
    
    
    d = []
    cnt = 0

    d.append(l[0])
    for i in range(1, 20):
        flag = -1
        for j in range(i):
            if d[j] > l[i]:
                flag = j
                break
        
        if flag == -1:
            d.append(l[i])
            continue
        
        cnt += i - j
        d.append(l[i])
        d.sort()
    print(t, cnt)
