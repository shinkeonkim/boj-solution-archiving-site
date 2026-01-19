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
  input()
  
  A = mii()
  B = mii()
  
  cnt = int(16 * min(A[0] / 8, A[1] / 8, A[2] / 4, A[3], A[4]/ 9))
  z = B[0] + B[1] // 30 + B[2] // 25 + B[3] // 10
  p(min(cnt, z))
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
