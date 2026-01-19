import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  l = mii()
  
  ans = 0
  crt = k
  
  for i in l:
    if i != crt:
      crt = k
  
    if i == crt:
      crt -= 1
    else:
      crt = k

    if crt == 0:
      ans += 1
      crt = k
  if crt == 0:
    ans += 1

  return ans
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
    p(f"Case #{t}: {d}")