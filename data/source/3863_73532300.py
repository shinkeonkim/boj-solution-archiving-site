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


def dup(A, B):
  A = [A[0], A[0] + A[1]]
  B = [B[0], B[0] + B[1]]
  
  return (max(A[0], B[0]), min(A[1], B[1]))


def solve():
  while 1:
    n, m = mii()
    if n == m == 0:
      break
    
    calls = [mii() for _ in range(n)]
    segs = [mii() for _ in range(m)]
    
    for seg in segs:
      cnt = 0
      for call in calls:
        dup_seg = dup(seg, call[2:])
        if dup_seg[1] - dup_seg[0] >= 1:
          cnt += 1
      p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

