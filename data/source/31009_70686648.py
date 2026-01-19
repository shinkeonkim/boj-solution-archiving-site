import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
l = [input().split() for i in range(n)]

k = 0
for i in l:
  if i[0] == "jinju":
    k = int(i[1])

cnt = 0
for i in l:
  cnt += int(int(i[1]) > k)

print(k)
print(cnt)