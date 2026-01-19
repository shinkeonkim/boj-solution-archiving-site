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


def solve():
  n, d = mii()
  
  ans = []
  if n % 2 == 0:
    for i in range(1, n // 2 + 1):
      ans.append(d + i)
      ans.append(d - i)
  else:
    ans.append(d)
    
    for i in range(1, n // 2 + 1):
      ans.append(d + i)
      ans.append(d - i)
  p(*ans)
      

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
