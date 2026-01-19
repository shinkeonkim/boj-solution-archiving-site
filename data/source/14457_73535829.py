import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  
  l = [[*map(int, list(input()))] for _ in range(n)]
  
  cnt = 0
  
  for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      if l[i][j] == 1:
        cnt += 1
        for y in range(i + 1):
          for x in range(j + 1):
            l[y][x] = 1 - l[y][x]
  
  p(cnt)
  
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

