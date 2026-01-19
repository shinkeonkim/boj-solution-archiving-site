import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  tc = 0
  while 1:
    n = ii()
    tc += 1
    if n == 0:
      break
    
    p(f"SET {tc}")
    l = [input() for _ in range(n)]
    
    ans = []
    ans2 = []
    for i in range(0, n, 2):
      ans.append(l[i])
    
    for i in range(1, n, 2):
      ans2.append(l[i])
    
    for i in ans:
      p(i)
    for i in ans2[::-1]:
      p(i)
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    