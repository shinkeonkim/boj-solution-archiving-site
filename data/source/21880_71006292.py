import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a, b = mii()
  
  _a = a
  _b = b
  
  if a > b:
    _a -= 1
  else:
    _b -= 1
  
  for i in range(1, _a + 1):
    p(f"{i}:0")
  for i in range(1, _b + 1):
    p(f"{_a}:{i}")
  p(f"{a}:{b}")
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
