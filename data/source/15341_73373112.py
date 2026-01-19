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


def solve():
  while True:
    s = input().replace(" ", "")
    if s == "0" * 16:
      break
    
    l = [*map(int, list(s))]
    
    for i in range(0, 16, 2):
      l[i] *= 2
      if l[i] > 9:
        l[i] -= 9
    
    sm = sum(l)
    
    if sm % 10 == 0:
      p("Yes")
    else:
      p("No")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
