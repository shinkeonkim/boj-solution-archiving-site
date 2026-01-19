n, m = map(int, input().split())
s = [*map(int, input().split())] + [0] * m

t = [[*map(int, input().split())] for i in range(n)]

for i in range(n):
  for j in range(n + m):
    s[i] -= t[i][j]
    s[j] += t[i][j]

print(*s)
