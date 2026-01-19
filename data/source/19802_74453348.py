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
  l = input().split()
  ans = ""
  for s in l:
    f = 0
    b = 0
    
    for i in range(len(s)):
      if s[i] == "'":
        f += 1
      else:
        break
    for i in range(len(s) - 1, -1, -1):
      if s[i] == "'":
        b += 1
      else:
        break
    
    s2 = s[2 * f:]
    
    if b > 0:
      s2 = s2[:-(2 * b)]
    
    ans += s2
  p(ans)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
