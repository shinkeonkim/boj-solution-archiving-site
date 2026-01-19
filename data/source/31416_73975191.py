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
  T_a, T_b, V_a, V_b = mii()
  
  X = T_b * V_b
  ans = 1111111111111111111111111
  for i in range(V_a + 1):
    j = V_a - i
    
    # i: 숙련된
    # j: 초보
    
    ans = min(ans, max(X + T_a * i, j * T_a))
  p(ans)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
