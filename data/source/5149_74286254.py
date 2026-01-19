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
  n, m = mii() # n: 역, m: 통과 역
  
  stations = [mii() for _ in range(n)]
  
  must = [i - 1 for i in mii()]
  
  first = stations[must[0]]
  rng = [[first[0], first[0]], [first[1], first[1]]]
  
  for i in range(m):
    here = stations[must[i]]
    
    rng[0][0] = min(rng[0][0], here[0])
    rng[0][1] = max(rng[0][1], here[0])
    rng[1][0] = min(rng[1][0], here[1])
    rng[1][1] = max(rng[1][1], here[1])
  
  ans = 0
  for i in range(n):
    here = stations[i]
    
    if rng[0][0] <= here[0] <= rng[0][1] and rng[1][0] <= here[1] <= rng[1][1]:
      ans += 1
  
  return ans
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(ret)
    p()