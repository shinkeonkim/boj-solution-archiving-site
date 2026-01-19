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
  while 1:
    h, w = mii()
    
    if h == w == 0:
      break

    keys = [inp() for _ in range(h)]
    
    positions = {}
  
    for i in range(h):
      for j in range(w):
        if keys[i][j] == '_':
          continue
        
        positions[keys[i][j]] = (i, j)
    
    query = inp()
    
    ans = len(query)
    prev = (0, 0)
    for i in query:
      here = positions[i]
      
      ans += abs(here[0] - prev[0]) + abs(here[1] - prev[1])
      
      prev = here
    
    p(ans)
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    
