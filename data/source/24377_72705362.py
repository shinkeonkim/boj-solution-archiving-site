import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l):
  idx = l.index(0)
  k = 10 - sum(l)
  
  p(idx + 1, k)

def g(l):
  p(*{1, 2, 3, 4}.difference(set(l)))
  

def solve():
  l = mii()
  
  zero = l.count(0)
  
  if zero == 0:
    print(*l[:2])
  elif zero == 1:
    f(l)
  else:
    g(l)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()