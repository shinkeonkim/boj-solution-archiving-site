import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n = ii()
  
  s = ""
  
  for i in range(n):
    s += inp().replace(" ", "")
  
  s2 = ""
  
  for i in s:
    if i in s2:
      continue
    s2 += i
  
  p(s2)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
