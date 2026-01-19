x = {}
y = {}

l = []
for i in range(int(input())):
    a, b = map(int, input().split())
    l.append([a, b])
    try:
        x[a] += 1
    except:
        x[a] = 1
    
    try:
        y[b] += 1
    except:
        y[b] = 1

ans = 0
for a, b in l:
    if y[b] > 1 and x[a] > 1:
        ans += (y[b] - 1) * (x[a] - 1)

print(ans)