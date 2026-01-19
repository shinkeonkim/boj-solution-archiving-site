import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
s = inp()
cnt = {}

for i in s:
  if i == " ":
    continue
  
  cnt[i] = cnt.get(i, 0) + 1

print(max(cnt.values()))