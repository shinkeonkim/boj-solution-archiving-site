import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

k = 2018 * 12 + 3
y = ii()

for i in range(12):
  z = y * 12  + i
  
  if(z - k) % 26 == 0:
    print("yes")
    break
else:
  print("no")