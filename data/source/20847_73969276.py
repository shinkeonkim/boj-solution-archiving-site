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


def solve():
  n = ii()
  l = [input().split() for _ in range(n)]
  
  l.sort(key = lambda t : (-int(t[1]), t[0]))
  
  s = []
  d = {}
  for i in l:
    if d.get(i[2], 0) == 0:
      d[i[2]] = 1
      s.append(i[0])
  
  p(len(s))
  
  s.sort()
  p(*s, sep="\n")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
