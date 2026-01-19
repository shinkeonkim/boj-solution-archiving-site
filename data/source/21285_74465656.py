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


def diff(a, b):
  ret= 0
  for i in range(len(a)):
    if a[i] != b[i]:
      ret += 1
  
  return ret


def solve():
  s = inp()
  n = ii()
  l = [inp() for _ in range(n)]
  
  for i in range(n):
    if len(l[i]) != len(s):
      continue
    
    if diff(l[i], s) <= 1:
      p(i + 1)
      break
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
