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

def to_t(s):
  h, m = map(int, s.split(":"))
  
  return h * 60 + m
  

def solve():
  st, en = map(to_t, input().split())
  
  N, T = mii()
  
  crt = st
  day = 0

  for i in range(N + 1):
    if crt + T >= en:
      day += 1
      crt = st + T
    else:
      crt += T

  p(day)
  p(f"{crt//60:02d}:{crt%60:02d}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

