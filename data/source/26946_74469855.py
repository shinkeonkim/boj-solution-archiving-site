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
  n, d = mii()
  
  l = mii()
  
  chk = [0] * n
  
  for i in l:
    chk[i - 1] = 1
  
  for _ in range(d):
    for i in range(n):
      if chk[i] == 1:
        continue
      if i - 1 >= 0:
        if chk[i - 1] == 1:
          chk[i] = 2
      if i + 1 < n:
        if chk[i + 1] == 1:
          chk[i] = 2
    for i in range(n):
      if chk[i] == 2:
        chk[i] = 1
  
  p(sum(chk))
  
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
