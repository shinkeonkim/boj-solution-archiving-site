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
  N, Q = mii()
  
  l = [ii() for _ in range(Q)]
  
  d = [0] * N
  
  cnt = 0
  for i in range(N):
    if i % 10 in [0, 3, 6]:
      d[i] = True
      cnt += 1
  
  for i in l:
    i -= 1
    if d[i]:
      cnt -= 1
    else:
      cnt += 1
    d[i] = not d[i]

    p(cnt)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
