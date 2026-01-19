import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(n):
  l = []
  
  while n > 0:
    l.append(n % 2)
    n //= 2
  while len(l) < 32:
    l.append(0)
  
  ret = 0
  z = 1
  for i in l[::-1]:
    ret += i * z
    z *= 2
  return ret

def solve():
  while 1:
    n = ii()
    if n == -1:
      break
    
    p(f(n))
    
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
