import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  
  l = s.split()
  
  cnt = 0
  for i in l:
    if "ae" in i:
      cnt += 1
  
  if cnt * 5 >= 2 * len(l):
    p("dae ae ju traeligt va")
  else:
    p("haer talar vi rikssvenska")
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
