import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  d = {}
  for _ in range(n):
    s = inp()
    d[s] = d.get(s, 0) + 1
    
  ans = 0
  
  for i in d.values():
    ans += (i - 1)
  
  p(ans)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
