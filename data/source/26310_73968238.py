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
  n = ii()
  
  l = [input().split() for _ in range(6)]
  z = []
  for i in range(6):
    name, *k = l[i]
    
    k = [*map(int, k)]
    
    score = k[3] * 56 + k[2] * 24 + k[1] * 14 + k[0] * 6 + k[4] * 30
    
    z.append([score, name])
  
  z.sort(key = lambda t : -t[0])

  idx = 0
  for i in range(6):
    if z[i][1] == 'Taiwan':
      idx = i
  
  cnt = [0] * 6
  for i in range(n):
    cnt[i % 6] += 1
  
  p(cnt[idx])
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    