import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


def f(a, b):
  if b[1] < a[0] or a[1] < b[0]:
    return (0, 0)
  return (max(a[0], b[0]), min(a[1], b[1]))


def g(x):
  return x[1] - x[0]


while 1:
  n = ii()
  if n == 0:
    break
    
  l = [mii() for _ in range(n)]
  x = (0, 4000)
  y = (0, 4000)
  z = (0, 4000)
  
  for i, j, k, d in l:
    x = f(x, (i, i + d))
    y = f(y, (j, j + d))
    z = f(z, (k, k + d))
  print(g(x) * g(y) * g(z))
