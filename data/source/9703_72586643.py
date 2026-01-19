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

def f(n, l):
  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        if l[i] - l[j] == l[j] - l[k]:
          return True
  return False
        

def solve():
  n = ii()
  l = mii()
  
  if f(n, l):
    return "NO"
  return "YES"
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")