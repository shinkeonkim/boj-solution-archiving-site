import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

l = mii()
d = []

for i in range(10):
  for j in range(i + 1, 10):
    d.append(l[i] or l[j])
    
for i in range(10):
  for j in range(i + 1, 10):
    for k in range(j + 1, 10):
      d.append(l[i] or l[j] or l[k])

k = d[0]

for i in range(1, len(d)):
  k ^= d[i]

print(k)