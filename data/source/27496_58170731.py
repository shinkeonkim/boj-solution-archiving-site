n, t = map(int, input().split())
l = [*map(int, input().split())]

s = [0] * n
s[0] = l[0]

for i in range(1, n):
    s[i] = l[i] + s[i - 1]

ans = 0
for i in range(0, n):
    sm = s[i] - (s[i - t] if i - t >= 0 else 0)
    
    if 129 <= sm <= 138:
        ans += 1
print(ans)