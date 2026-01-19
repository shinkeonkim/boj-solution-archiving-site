import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = []
  
  while len(l) < n * 2:
    _l = mii()
    l.extend(_l)
  
  ans = [0, 0]
  for i in range(n):
    a = l[i * 2]
    b = l[i * 2 + 1]
    
    if abs(a -  b) == 1:
      if a < b:
        if a == 1:
          ans[0] += 6
        else:
          ans[0] += a + b
      else:
        if b == 1:
          ans[1] += 6
        else:
          ans[1] += a + b
    else:
      if a > b:
        ans[0] += a
      elif a < b:
        ans[1] += b

  return ans
        
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    print(f"Game {t}: Tessa {ret[0]} Danny {ret[1]}")
