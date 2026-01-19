import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a, b, k = mii()
  ans = 0
  for i in range(a):
    for j in range(b):
      if i & j < k:
        ans += 1
  return ans
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    r = solve()
    print(f"Case #{t}: {r}")