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
  k = ii()
  
  a = inp()
  b = inp()
  n = len(a)
  
  same = 0
  diff = 0
  
  for i in range(n):
    if a[i] == b[i]:
      same += 1
    else:
      diff += 1
  
  same_ans = min(k, same)
  
  k -= same_ans
  
  diff_ans = diff - k
  
  p(same_ans + diff_ans)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
