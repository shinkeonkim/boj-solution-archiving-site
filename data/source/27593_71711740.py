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
  l = [0] + mii() + [1440]
  
  ans = 0

  for i in range(len(l) - 1):
    if l[i + 1] - l[i] >= 120:
      ans += (l[i + 1] - l[i]) // 120
  
  if ans >= 2:
    return "YES"
  return "NO"
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
