import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


t = ii()
l = [mii() for i in range(t)]

ans = 0


if l[0][1] == l[0][0] and l[0][0] != 0:
  ans += 1

for i in range(1, t):
  if l[i][0] != 0 and l[i][0] == l[i - 1][0]:
    ans += 1
  if l[i][1] != 0 and l[i][1] == l[i - 1][1]:
    ans += 1
  if l[i][1] == l[i][0] and l[i][0] != 0:
    ans += 1
print(ans)
