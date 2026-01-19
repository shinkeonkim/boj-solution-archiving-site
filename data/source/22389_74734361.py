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

  
def solve():
  while 1:
    n, l, r = mii()
    
    if n == l == r == 0:
      break
    
    A = [ii() for _ in range(n)]
    cnt = 0
    for x in range(l, r + 1):
      chk = True
      for i in range(n):
        if x % A[i] == 0:
          if i % 2 == 0:
            cnt += 1
            break
          else:
            chk = False
            break
      else:
        if chk and n % 2 == 0:
          cnt += 1
    p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
