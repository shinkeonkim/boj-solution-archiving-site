import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
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
  
  n, m = mii()
  A = mii()
  B = mii()
  
  A_S = sum(A)
  B_S = sum(B)
  cnt = 0
  for i in A:
    if (A_S - i) * n > A_S * (n - 1) and (B_S + i) * m > B_S * (m + 1):
      cnt += 1
  
  p(cnt)
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
