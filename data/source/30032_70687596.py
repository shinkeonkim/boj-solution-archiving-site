import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n, d = mii()
l = [input() for i in range(n)]

k = {}

if d == 1:
  k = {'d': 'q', 'b': 'p', 'q': 'd', 'p': 'b'}
else:
  k = {'d': 'b', 'b': 'd', 'q': 'p', 'p': 'q'}

for i in l:
  for j in i:
    print(end=k[j])
  print()