import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  tc = 1
  while 1:
    n = ii()
    
    n = int(n / 2 + 0.5)
    
    n = int(n * 3 / 2 + 0.5)
    if n == 0:
      break
    k = n // 62 + int(n % 62 > 0)
    d = k // 30000 + int(k % 30000 > 0)
    
    p(f"File #{tc}")
    p(f"John needs {d} floppies.\n")
    tc += 1

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
