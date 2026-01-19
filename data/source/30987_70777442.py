import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(x, a, b, c, d, e):
  return (a // 3) * (x ** 3) + (b - d) // 2 * x * x + (c - e) * x

def solve():
  x1, x2 = mii()
  a, b, c, d, e = mii()
  
  print(f(x2, a, b, c, d, e) - f(x1, a, b, c, d, e))
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    