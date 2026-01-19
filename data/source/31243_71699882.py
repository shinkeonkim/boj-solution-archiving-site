import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  mx = 0
  mn = 1111111111111111

  for i in range(3):
    a, b, c, d = mii()
    x = a * 60 + b
    y = c * 60 + d

    if x < y:
      d = y - x
    else:
      d = 1440 - x + y

    mx = max(mx, d)
    mn = min(mn, d)

  print(f"{mn//60}:{mn%60:02d}")
  print(f"{mx//60}:{mx%60:02d}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()