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

def dup(a, b):
  if b[0] <= a[1]:
    return True

def solve():
  l = [mii() for _ in range(3)]
  
  mn = min([i[1] - i[0] for i in l])
  mx = max([i[1] - i[0] for i in l])
  
  l.sort(key = lambda t:(t[0], -t[1]))
  cnt = 3
  
  for i in range(1, 3):
    if dup(l[i - 1], l[i]):
      l[i] = [min(l[i][0], l[i-1][0]), max(l[i][1], l[i-1][1])]
      cnt -= 1
  
  p(cnt)
  p(mn, mx)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    