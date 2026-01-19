import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  K, b, n = mii()
  
  l = []
  
  while n > 0:
    l.append(n % b)
    n //= b
  
  p(K, sum([i * i for i in l]))
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
