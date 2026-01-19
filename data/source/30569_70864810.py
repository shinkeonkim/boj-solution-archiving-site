import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


h1, d1, t1 = mii()
h2, d2, t2 = mii()

crt = 0

h1 -= d2
h2 -= d1

while h1 > 0 and h2 > 0:
  k1 = t1 - crt % t1
  k2 = t2 - crt % t2
  
  if k1 == k2:
    h1 -= d2
    h2 -= d1
    crt += k1
  elif k1 < k2:
    h2 -= d1
    crt += k1
  else:
    h1 -= d2
    crt += k2

if h1 <= 0 and h2 <= 0:
  print("draw")  
elif h1 > 0:
  print("player one")
else:
  print("player two")

