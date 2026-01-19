import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def ln(n):
  return n // 3 if n % 3 == 0 else n // 3 + 1

def rev(s):
  return s[::-1]

def tail(s):
  return s[1:]

def pre(s):
  return s[:ln(len(s))]

def solve():
  s = input()
  
  x = pre(s)
  
  k1 = x + rev(x) + x
  k2 = x + tail(rev(x)) + x
  k3 = x + rev(x) + tail(x)
  k4 = x + tail(rev(x)) + tail(x)
  
  if s in [k1, k2, k3, k4]:
    p(1)
  else:
    p(0)
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
