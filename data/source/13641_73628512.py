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


def solve():
  while 1:
    try:
      n = ii()
      a = mii()
      b = mii()
    except:
      break
    
    A = [0] * n
    B = [0] * n
    
    for i in range(n):
      A[a[i] - 1] = i
      B[b[i] - 1] = i
    
    cnt = 0
    for i in range(n):
      for j in range(i + 1, n):
        x = (A[i], B[i])
        y = (A[j], B[j])
        
        if x[0] < y[0] and x[1] > y[1]:
          cnt += 1
        elif x[0] > y[0] and x[1] < y[1]:
          cnt += 1
    p(cnt)
  
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

