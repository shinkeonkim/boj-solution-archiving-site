import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(num):
  d = 1
  
  while d < num:
    d *= 2
  
  return d


def solve():
  while 1:
    G, T, A, D = mii()
    
    if G == T == A == D == -1:
      break
    
    z = A * G + D
    z2 = f(z)
    
    Y = z2 - z
    
    X = z2 - 1 + (T * (T - 1) * G // 2)
    
    p(f"{G}*{A}/{T}+{D}={X}+{Y}")
      

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
