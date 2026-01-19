import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(num, k):
  l = []
  
  while num > 0:
    l.append(num % k)
    num //= k
  
  return l[::-1]
  

def g(ar):
  ret = 0
  for i in range(len(ar) - 1):
    if ar[i] != ar[i + 1]:
      ret += 1
  return ret
  

def solve():
  k = ii()
  
  ans = 0
  mn = 1111111111111
  for i in range(2, 11):
    comp = g(f(k, i))
    
    if mn >= comp:
      mn = comp
      ans = i
  p(ans)  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

