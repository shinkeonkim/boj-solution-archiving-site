import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  return f(b, a % b) if b > 0 else a

def solve():
  while 1:
    a, b, c, d = mii()
    if a == b == c == d == 0:
      break
    
    k = f(a, b)
    k = f(k, c)
    k = f(k, d)
  
    p(k)

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
