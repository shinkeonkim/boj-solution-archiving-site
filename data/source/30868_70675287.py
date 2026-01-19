import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

for _ in range(ii()):
  n = ii()
  
  a = n // 5
  b = n % 5
  
  if a > 0:
    print("++++ " * a, end="")
  print("|" * b)