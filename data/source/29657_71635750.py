import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a, b, c = map(int, input().split())
  x, y, z = map(int, input().split())
  h, m, s = map(int, input().split())

  t = h * b * c + m * c + s
  
  t %= x * y * z

  print((t // (y * z)), (t % (y * z)) // z, (t % (y * z)) % z)
    

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
