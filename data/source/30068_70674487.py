import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
l = [mii() +[i] for i in range(n)]
l.sort(key = lambda t: (t[1], t[0]))
ans = []
for i in range(1, n):
  if l[i - 1][1] != l[i][1]:
    continue
  ans.append([l[i][1], l[i][0] - l[i-1][0], l[i][2]])
ans.sort(key = lambda t: t[2])

for i in ans:
  print(*i[:-1])