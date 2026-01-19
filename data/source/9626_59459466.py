n, m = map(int, input().split())
u, l, r, d = map(int, input().split())
s = [input() for i in range(n)]

s2 = "#."

c = l + r + m
ans = [(s2 * m * 2)[i % 2 :i % 2 + c]  for i in range(u + d + n)]

for i in range(0, n):
    for j in range(0, m):
        ans[i+u] = ans[i+u][:j+l] + s[i][j] + ans[i+u][j+l+1:]

print(*ans, sep="\n")