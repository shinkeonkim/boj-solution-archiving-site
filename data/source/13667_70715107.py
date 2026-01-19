import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def f(l):
  idx = []
  
  for i in range(5):
    if l[i] <= 127:
      idx.append(i)
  
  if len(idx) != 1:
    return "*"

  return chr(idx[0] + 65)

while 1:
  n = ii()
  
  if n == 0:
    break
  
  l = [mii() for _ in range(n)]
  
  for i in l:
    print(f(i))