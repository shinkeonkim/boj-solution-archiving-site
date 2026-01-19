import sys
from math import sqrt, pi, sin, factorial
from decimal import *

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  if a[0] < b[0] and a[1] > b[1]:
    return True
  
  if a[0] > b[0] and a[1] < b[1]:
    return True
  
  return False


def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  cnt = 0
  
  for i in range(n):
    for j in range(i + 1, n):
      if(f(l[i], l[j])):
        cnt += 1
  return cnt

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")
