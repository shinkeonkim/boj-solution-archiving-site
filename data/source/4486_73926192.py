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
  tc = 1
  while 1:
    n = ii()
    
    if n == 0:
      break
  
    ans = []
    for i in range(1, 257):
      for j in range(1, 257):
        if i + j >= n:
          break
        k = n - (i + j)
        price = i * 16 + j * 2 + k

        # 1개 -> 4센트   -> 16
        # 1개 -> 1 / 2센트 -> 2
        # 1개 -> 1 / 4센트 -> 1
        if price != n * 4:
          continue
        
        ans.append([i, j, k])
    
    p(f"Case {tc}:")
    p(f"{n} pencils for {n} cents")
    
    if len(ans) == 0:
      p("No solution found.")
      p()
    else:
      for a, b, c in ans:
        p(f"{a} at four cents each")
        p(f"{b} at two for a penny")
        p(f"{c} at four for a penny")
        p()

    tc += 1
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
