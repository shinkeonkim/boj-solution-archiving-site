import sys
from math import sqrt, pi, sin, factorial
inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(n, a, b):
  A = a + b - n
  B = min(a, b)
  mx = max(A, B)
  mn = min(A, B)
  
  return (mn, mx)


def solve():
  flag = ii()
  
  n, a, b, c = mii()
  
  z = f(n, a, b)
  
  l = [*f(n, z[0], c), *f(n, z[1], c)]
  
  if flag == 1:
    p(max(min(l), 0))
  else:
    p(max(max(l), 0))


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
