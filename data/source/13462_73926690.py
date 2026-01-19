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
  s = input()
  
  i = 0
  ans = ""
  while i < len(s):
    if i + 2 < len(s):
      z = set(s[i:i+3])
      
      if len(z) == 3:
        ans += "C"
        i += 3
        continue
    
    ans += {"R": "S", "B": "K", "L": "H"}[s[i]]
    i += 1

  p(ans)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
