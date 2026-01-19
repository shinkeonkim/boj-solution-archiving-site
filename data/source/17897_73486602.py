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
  n = ii()
  
  names = []
  ans = []

  for idx in range(n):
    k = ii()
    names.append(input())
    
    chk = 0
    
    for __ in range(k):
      s = input()
      
      if "pea soup" == s:
        chk |= 1
      if "pancakes" == s:
        chk |= 2
    
    if chk == 3:
      ans.append(idx)
    
  if len(ans) == 0:
    p("Anywhere is fine I guess")
  else:
    p(names[ans[0]])
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
