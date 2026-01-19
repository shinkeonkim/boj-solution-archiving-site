import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a, *a_l = mii()
  b, *b_l = mii()
  

  cnt = [['A', 0, 0, 0, 0], ['B', 0, 0, 0, 0]]
  
  for i in a_l:
    cnt[0][i] += 1
  
  for j in b_l:
    cnt[1][j] += 1
  
  cnt.sort(key = lambda t: (-t[4], -t[3], -t[2], -t[1]))
  
  if cnt[0][1:] == cnt[1][1:]:
    print("D")
  else:
    print(cnt[0][0])
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
