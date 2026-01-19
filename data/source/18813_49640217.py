n, m = map(int, input().split())
l = [input() for i in range(n)]
ans = 0

for s in l:
    ss = set([*s])
    if len(ss) != len(s):
        continue
    
    for i in s:
        if ord(i) - 64 > m:
            break
    else:
        ans += 1

print(ans)
 