import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
a = []
b = []
l = [inp().split() for i in range(n)]

for i in l:
  k = int(i[1])
  if i[0] == 'M':
    a.append(k)
  else:
    b.append(k)

if len(a) == 0:
  a.append(0)
if len(b) == 0:
  b.append(0)
    
print("M" if sum(a) * len(b) > sum(b) * len(a) else ("J" if sum(a) * len(b) < sum(b) * len(a) else "V"))
