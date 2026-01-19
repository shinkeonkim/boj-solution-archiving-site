import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  x, *a = mii()
  y, *b = mii()
  
  ans = 11111111111111111
  for i in a:
    for j in b:
      ans = min(ans, abs(i - j))
  return ans
    
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    ret = solve()
    print(ret)    