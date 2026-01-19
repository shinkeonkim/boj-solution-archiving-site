import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  

def solve():
  n = ii()
  
  z = 1
  while z < n:
    z *= 2
  
  base = len(bin(z)[2:])
  
  k = bin(n)[2:]
  
  k = "0" * (base - len(k)) + k
  
  idx = 0
  for i in range(len(k) - 1, -1, -1):
    if k[i] == '1':
      idx = i
      break
  
  p(idx)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
   