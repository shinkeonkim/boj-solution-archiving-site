import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  p = sorted(mii())
  c = mii()

  x = sum(p) * c[0]

  mx = 0
  for i in range(3):
    for j in range(3):
      if i == j:
        continue
      mx = max(mx, p[i] * c[1] + p[j] * c[2])

  if x > mx:
    print(f"one {x/100:.2f}")
    # print(f"one {x//100}.{x%100:02d}")
  else:
    print(f"two {mx/100:.2f}")
    # print(f"two {mx//100}.{mx%100:02d}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()