import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  return (max(a[0], b[0]), min(a[1], b[1]))

def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  x = l[0][:2]
  y = l[0][2:]
  
  for i in range(1, n):
    crt = l[i]
    
    x = f(x, crt[0:2])
    y = f(y, crt[2:])
    
  if x[0] > x[1] or y[0] > y[1]:
    return 0
  return (x[1] - x[0]) * (y[1] - y[0])

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)

