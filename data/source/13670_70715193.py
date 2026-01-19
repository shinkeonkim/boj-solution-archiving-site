import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

while 1:
  h1, m1, h2, m2 = mii()
  
  if h1 == m1 == h2 == m2 == 0:
    break
    
  t1 = h1 * 60 + m1
  t2 = h2 * 60 + m2
  
  if t1 < t2:
    print(t2 - t1)
  else:
    print(1440 - t1 + t2)