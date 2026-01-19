import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  h, w = mii()
  
  l = [mii() for _ in range(h)]
  
  mn = 11111111111111111111111
  for i in range(h):
    for j in range(w):
      cnt = 0
      
      for y in range(h):
        for x in range(w):
          cnt += l[y][x] * min(abs(y - i), abs(x - j))
      mn = min(mn, cnt)
  print(mn)
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
