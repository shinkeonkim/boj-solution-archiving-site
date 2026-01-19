import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  r, c = mii()
  
  l = [inp() for _ in range(r)]
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  mx = 0
  ans = [0, 0]
  
  for y in range(r):
    for x in range(c):
      cnt = 0
      
      if l[y][x] == '@':
        continue

      for d in range(4):
        a, b = y, x
        while a >= 0 and b >= 0 and a < r and b < c:
          if l[a][b] == '#':
            break
          if l[a][b] == '@':
            cnt += 1
          a += dy[d]
          b += dx[d]
        
      if mx < cnt:
        mx = cnt
        ans = [y, x]
  p(f"{ans[0]}, {ans[1]}")
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
