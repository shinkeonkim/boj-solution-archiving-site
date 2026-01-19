import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  x = y = 0
  ans = []
  mx = 0
  
  while 1:
    a, b = mii()
    if a == b == 0:
      break
    
    x += a
    y += b
    
    if mx < x * x + y * y:
      mx = x * x + y * y
      ans = [x, y]
    if mx == x * x + y * y and ans[0] < x:
      ans = [x, y]

  print(*ans)
    
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
