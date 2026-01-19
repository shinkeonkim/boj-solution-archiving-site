import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def f(x, y):
  if x == 0 or y == 0:
    return "divisa"
  
  if x > 0:
    return ("NE" if y > 0 else "SE")
  else:
    return ("NO" if y > 0 else "SO")
      
while 1:
  n = ii()
  
  if n == 0:
    break
    
  k = mii()
  
  l = [mii() for i in range(n)]
  
  for i in l:
    print(f(i[0] - k[0], i[1] - k[1]))