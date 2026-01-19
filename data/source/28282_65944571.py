x, k = map(int, input().split())

l = [*map(int, input().split())]
d = {}

for i in range(x):
    try:
        d[l[i]] += 1
    except:
        d[l[i]] = 1

ans = 0

for i in range(x, 2*x):
    ans += x - d.get(l[i], 0)

print(ans)