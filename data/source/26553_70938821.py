import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  k, p, x = mii()
  ans = 1000000000000000000
  for m in range(1, 100000):
    money = m * x + k / m * p
    ans = min(ans, money)
  print(f"{ans:.3f}")
    
        
if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    solve()

    