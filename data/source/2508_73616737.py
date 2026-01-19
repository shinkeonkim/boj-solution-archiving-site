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
  input()
  r, c = mii()
  
  l = [input() for _ in range(r)]
  cnt = 0

  for i in range(r):
    for j in range(1, c - 1):
      if l[i][j-1:j+2] == '>o<':
        cnt += 1
  
  
  for i in range(1, r - 1):
    for j in range(0, c):
      if l[i][j] == 'o' and l[i-1][j] == 'v' and l[i+1][j] == '^':
        cnt += 1
      
  p(cnt)  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

