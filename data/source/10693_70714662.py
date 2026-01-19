import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())

for tc in range(ii()):
  n, m = mii()
  print(f"Case {tc+1}: {max(0, m - n + 1)}")