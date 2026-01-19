import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  
def f(l):
  n = len(l)
  for i in range(n):
    for j in range(n - 1):
      if l[i][j] >= l[i][j + 1]:
        return False
  
  for i in range(n - 1):
    for j in range(n):
      if l[i][j] >= l[i + 1][j]:
        return False
  return True
      
  
  
def pr(l):
  for i in l:
    p(*i)

def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  for _ in range(4):
    if f(l):
      pr(l)
      break

    l2 = []

    for j in range(n - 1, -1, -1):
      _l2 = []
      for i in range(n):
        _l2.append(l[i][j])
      l2.append(_l2)
    
    l = l2
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
