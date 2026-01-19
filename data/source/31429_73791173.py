import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  l = [
    [12, 1600], [11, 894], [11, 1327], [10, 1311],
    [9, 1004], [9, 1178], [9, 1357], 
    [8, 837], [7, 1055], [6, 556], [6, 773]
  ]

  p(*l[ii() - 1])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()