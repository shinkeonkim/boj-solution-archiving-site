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


def dis(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve():
  n = ii()
  
  point = mii()
  s = point[:2]
  e = point[2:]
  
  ret = []

  for _ in range(n):
    m = ii()
    path = [s[::]] + [mii() for _ in range(m)] + [e[::]]
    cnt = 0
    for i in range(len(path) - 1):
      cnt += dis(path[i], path[i +1])
  
    ret.append(cnt)
    
  p(ret.index(min(ret)) + 1)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
