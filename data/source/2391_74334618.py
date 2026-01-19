import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  ret = 0
  for i in range(len(a)):
    if a[i] == b[i]:
      continue
    ret += 1
  return ret


def solve():
  s = input()
  w = ii()
  l = [input() for _ in range(w)]
  
  ans = 0
  crt = 200

  for i in range(w):
    diff = f(l[i], s)
    
    if diff < crt:
      crt = diff
      ans = i
  
  p(l[ans])
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
