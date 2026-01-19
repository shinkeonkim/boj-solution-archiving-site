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

def clockwise(n, st, en):
  if st >= en:
    return st - en
  
  return n - en + st

def anticlockwise(n, st, en):
  if st <= en:
    return en - st
  
  return n - st + en

def solve():
  while 1:
    n, t1, t2, t3 = mii()
    
    if n == t1 == t2 == t3 == 0:
      break
    
    mx = 0
    for start in range(0, n):
      ans = 3 * n
      ans += clockwise(n, start, t1)
      ans += anticlockwise(n, t1, t2)
      ans += clockwise(n, t2, t3)
      
      mx = max(mx, ans)
    p(mx)
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
