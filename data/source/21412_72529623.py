import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  return f(b, a % b) if b else a

def solve():
  n = ii()
  mx = 0

  for i in range(1, n):
    a = i
    b = n - i

    if a >= b:
      break

    if f(a, b) == 1:
      mx = i
  print(mx, n - mx)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()