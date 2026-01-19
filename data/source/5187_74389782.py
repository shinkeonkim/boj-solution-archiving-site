import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  m, n = mii() # m : 물질 수? n: 직사각형 수?
  
  materials = [ii() for _ in range(m)]
  oblongs = [mii() for _ in range(n)]
  
  ans = 0
  for i in range(n):
    vol = oblongs[i][0] * oblongs[i][1] * oblongs[i][2]
    ans += materials[oblongs[i][3] - 1] * vol
  
  p(ans)
  
  
tc = ii()

for t in range(1, tc+1):
  p(f"Data Set {t}:")
  ret = solve()
  
