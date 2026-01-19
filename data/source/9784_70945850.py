import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, p, q = mii()
  l = sorted(mii())
  
  w = i = j = 0
  while i < n and j < p and w < q:
    crt = l[i]
    
    if w + crt <= q:
      w += crt
      j += 1
    i += 1
  return j
  
    
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case {t}: {ret}")
    