import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(chk, month, day):
  k = f"{month}{day}"
  for i in k:
    if chk[ord(i) - 48] == 1:
      return False
  return True


def solve():
  chk = mii()
  ans = 0
  days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  for month in range(1, 13):
    
    day = days[month - 1]
    
    for d in range(1, day + 1):
      if f(chk, month, d):
        ans += 1
  p(ans)

  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
