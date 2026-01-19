import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = mii()
ans = 0

for i in range(n):
  for j in range(i, n):
    s = sum(l[i:j+1])
    cnt = j - i + 1
    
    if s % cnt:
      continue

    ans += int(l[i:j+1].count(s // cnt) > 0)
print(ans)