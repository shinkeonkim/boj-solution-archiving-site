import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n = ii()

  k = n // 2

  for i in range(n // 2):
    d = 2 * i + 1
    print("*" * d + " " * (2 * (n - d)) + "*" * d)

  for i in range(n // 2, -1, -1):
    d = 2 * i + 1
    print("*" * d + " " * (2 * (n - d)) + "*" * d)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()