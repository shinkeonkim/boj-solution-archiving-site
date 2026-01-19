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

def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a

def lcm(a, b):
  return a * b // gcd(a, b)

def solve():
  N, L, H = mii()
  l = mii() # N개
  
  for i in range(L, H + 1):
    for j in l:
      if i % j == 0 or j % i == 0:
        continue
      break
    else:
      return i
  
  return "NO"
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")