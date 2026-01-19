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


def check(query, datum, sz):
  for i in range(sz):
    if query[i] == -1:
      continue
    
    if query[i] != datum[i]:
      return False
  return True
  

def solve():
  n, m = mii()
  data = [mii() for _ in range(n)]
  
  q = ii()
  
  queries = [mii() for _ in range(q)]
  
  for query in queries:
    cnt = 0
    for datum in data:
      if check(query, datum, m):
        cnt += 1
    p(cnt)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
