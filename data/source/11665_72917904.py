import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def inter(a, b):
  return [max(a[0], b[0]), min(a[1], b[1])]


def solve():
  X = [-1000, 2000]
  Y = [-1000, 2000]
  Z = [-1000, 2000]
  for _ in range(ii()):
    l = mii()
    
    X = inter(X, [l[0], l[3]])
    Y = inter(Y, [l[1], l[4]])
    Z = inter(Z, [l[2], l[5]])
    
  X = max(0, X[1] - X[0])
  Y = max(0, Y[1] - Y[0])
  Z = max(0, Z[1] - Z[0])
  
  p(X * Y * Z)
  
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
