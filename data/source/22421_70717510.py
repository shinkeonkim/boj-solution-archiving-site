import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

while 1:
  n, cost = mii()
  
  if n == cost == 0:
    break
  
  ans = 11111111111111111111

  for a in range(0, n):
    b = n - a
    ans = min(ans, abs(sqrt(a * a + b * b) - cost))
  print(ans)
