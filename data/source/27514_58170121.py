n = int(input())
l = sorted([*map(int, input().split())])

d = {}

for i in l:
    try:
        d[i] += 1
    except:
        d[i] = 1

crt = 1
ans = max(l)

for i in range(300):
    if crt in d:
        cnt = d[crt] // 2
        
        if d[crt] > 0:
            ans = max(ans, crt)

        if cnt == 0:
            continue
        try:
            d[crt * 2] += cnt
        except:
            d[crt * 2] = cnt
            
    crt *= 2

print(ans)