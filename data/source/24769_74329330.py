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


def solve():
  while 1:
    n = ii()
    
    if n == 0:
      break

    l = [inp() for _ in range(n)]
    
    ans = l[0]
    mx = 0
    for s in l:
      idx = 0
      cnt = 0
      while idx + 1 < len(s):
        if s[idx] in 'aeiouy' and s[idx] == s[idx + 1]:
          cnt += 1
          idx += 1
        idx += 1
      
      if mx < cnt:
        mx = cnt
        ans = s
    p(ans)

    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
