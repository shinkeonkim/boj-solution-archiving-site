import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = input().split()
  s = input()
  k = ii() - 1
  
  n = len(l)
  
  start = 0
  
  for i in range(n):
    if l[i] == s:
      start = i
  
  k += start
  k = (k + n) % n
  
  p(l[k])
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
