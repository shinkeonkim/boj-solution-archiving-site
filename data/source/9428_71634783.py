import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  sm, sy = mii()
  em, ey = mii()

  m = sm
  y = sy
  ans = 0
  
  if sy == ey:
    print("{0:0.4f}".format((em - sm) / 2 / (13 - sm)))
    return
    
  ans += 12
  m = 1
  y += 1
  

  while y * 12 + m < ey * 12 + em:
    if y < ey:
      y += 1
      m = 1
      ans += 24
      continue
    
    ans += 2    
    m += 1

  print(f"{ans / 24:.4f}")
    

if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    solve()
