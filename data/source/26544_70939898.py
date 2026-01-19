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
  w = mii()
  h = mii()
  
  ans = 0
  ans += sum(w) * 2 + h[0] + h[-1]
  
  for i in range(1, n):
    ans += abs(h[i] - h[i - 1])
  
  p(ans)
  
        
if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    solve()

    