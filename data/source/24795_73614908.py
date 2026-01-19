import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  

def solve():
  N, Y = mii()
  l = sorted([*set([ii() for _ in range(Y)])]) + [-1]
  
  i = 0
  j = 0
  
  while i < N:
    if i == l[j]:
      j += 1
    else:
      p(i)
    i += 1
  
  p(f"Mario got {j} of the dangerous obstacles.")
      
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

