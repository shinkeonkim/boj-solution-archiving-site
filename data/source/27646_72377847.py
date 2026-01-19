import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = int(input())
  
  p(n - 1)
  for i in range(n - 1):
    p(0, i)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    input()
    ret = solve()

