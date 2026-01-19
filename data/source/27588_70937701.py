import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  r, c = mii()
  l = [mii() for _ in range(r)]
  ans = 111111111111111111111111
  
  for i in range(r):
    for j in range(c):
      k = 0
      for y in range(r):
        for x in range(c):
          k += (abs(i - y) + abs(j - x)) * l[y][x]
      ans = min(ans, k)
  print(ans)
  
  
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()
