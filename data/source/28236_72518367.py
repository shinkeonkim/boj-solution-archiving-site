import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m, k = mii()
  l = [mii() for _ in range(k)]
  
  target = [1, m + 1]
  
  ans = -1
  mn = 11111111111111
  for i in range(k):
    y, x = l[i]
    dis = abs(target[0] - y) + abs(target[1] - x)
    
    if dis < mn:
      mn = dis
      ans = i + 1
  p(ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   