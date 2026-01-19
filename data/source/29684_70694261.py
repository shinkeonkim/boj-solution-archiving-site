import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

while 1:
  n = ii()
  
  if n == 0:
    break
  
  l = mii()
  ans = 0

  for i in range(n):
    if abs(l[i] - 2023) < abs(l[ans] - 2023):
      ans = i
  print(ans + 1)