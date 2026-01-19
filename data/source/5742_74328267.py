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
  while 1:
    n, c, k = mii()

    if n == c == k == 0:
      break
    
    l = [mii() for _ in range(n)]
    
    d = {}
    
    for i in range(1, k + 1):
      d[i] = 0
    
    for i in l:
      for j in i:
        d[j] += 1

    mn = min(d.values())
    
    ans = []
    for i in range(1, k + 1):
      if d[i] == mn:
        ans.append(i)
    
    p(*ans)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
