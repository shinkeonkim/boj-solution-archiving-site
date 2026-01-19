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


def solve():
  n = ii()
  st = set()
  l = [mii() for _ in range(n)]
  
  for i in l:
    for j in i:
      st.add(j)
  
  st = [*st]
  if len(st) != n * n:
    return "FALSE"
  
  if min(st) != 1 or max(st) != n * n:
    return "FALSE"
  
  s = n * (n * n + 1) // 2
  
  for i in range(n):
    if sum(l[i]) != s:
      return "FALSE"
    
    if sum([l[j][i] for j in range(n)]) != s:
      return "FALSE"
  
  if sum([l[i][i] for i in range(n)]) != s:
    return "FALSE"

  if sum([l[i][n - i - 1] for i in range(n)]) != s:
    return "FALSE"
  
  return "TRUE"

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
    
