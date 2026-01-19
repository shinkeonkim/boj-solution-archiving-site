import sys
from math import sqrt, pi, sin, factorial
from decimal import *

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  cap = []
  crt = []
  
  for i in range(3):
    a, b = mii()
    cap.append(a)
    crt.append(b)
    
  
  idx = 0
  for _ in range(100):
    nxt = (idx + 1) % 3
    
    
    can_move = min(crt[idx], cap[nxt] - crt[nxt])
    
    crt[idx] -= can_move
    crt[nxt] += can_move  
  
    idx += 1
    idx %= 3
  p(*crt, sep="\n")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    d = solve()
