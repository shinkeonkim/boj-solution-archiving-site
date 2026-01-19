import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  while 1:
    l = mii()
    n, width, length, height, area, m = l
    if sum(l) == 0:
      break

    l = [mii() for _ in range(m)]

    k = (width + length) * height * 2 + (width * length)
    for a, b in l:
      k -= a * b

    k *= n

    print(k // area + int(k % area > 0))

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()