import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def solve():
  s = input()
  
  l = []
  for i in s:
    l.append(d[i])
  
  mx = 0
  ans = 0
  for i in l[::-1]:
    if i >= mx:
      ans += i
    else:
      ans -= i
    mx = max(mx, i)
  
  p(ans)
  
tc = ii()

for t in range(1, tc+1):
  ret = solve()
    