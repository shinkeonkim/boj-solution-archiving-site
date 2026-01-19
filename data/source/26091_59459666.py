n, m = map(int, input().split())
l = sorted([*map(int, input().split())])

s = 0
e = n - 1

ans = 0

while s < e:
    if l[s] + l[e] >= m:
        ans += 1
        s += 1
        e -= 1
    else:
        s += 1
print(ans)
