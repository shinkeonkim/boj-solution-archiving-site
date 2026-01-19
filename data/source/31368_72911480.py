import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()  
  
  l = [input() for _ in range(n)]
  
  cnt = [0, 0, 0]
  
  for i in l:
    if "blue" in i and "black" in i:
      cnt[0] += 1
    elif "white" in i and "gold" in i:
      cnt[1] += 1
    else:
      cnt[2] += 1
  
  for i in range(3):
    p(f"{100 * cnt[i] / sum(cnt):.7f}")
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
