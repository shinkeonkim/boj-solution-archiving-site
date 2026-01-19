import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def dis(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve():
  n = ii()
  a = ii()
  b = ii()
  
  center = (n // 2, n // 2)

  
  for i in range(n):
    for j in range(n):
      if a <= dis(center, (i, j)) <= b:
        p(end="*")
      else:
        p(end=".")
    p()
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()