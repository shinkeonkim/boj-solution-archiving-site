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
  m, n, i, j, c = mii()
  
  dis = abs(i - 1) + abs(j - 1)
  
  color = c if dis % 2 == 0 else 1 - c

  cnt = 0

  if m % 2 == 0:
    cnt += (m // 2) * n    
  else:
    cnt += (m // 2) * n
    
    cnt += (n // 2) + (n % 2)
  
  chk = [0, 0]
  chk[color] = cnt
  chk[1 - color] = m * n - cnt
  
  if chk[0] > chk[1]:
    p("black")
  elif chk[0] < chk[1]:
    p("white")
  else:
    p("equal")
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
