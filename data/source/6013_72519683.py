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

def f(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  mx = 0
  ans = []
  for i in range(n):
    for j in range(i + 1, n):
      dis = f(l[i], l[j])
      if mx < dis:
        mx = dis
        ans = [i + 1, j + 1]
  p(*ans)
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   