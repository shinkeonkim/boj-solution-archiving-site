import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, m = mii()
  a = mii()
  b = mii()

  ans = 0
  i = j = 0
  while i < n and j < m:
    if a[i] == b[j]:
      ans += 1
      i += 1
      j += 1
    elif a[i] < b[j]:
      i += 1
    else:
      j += 1

  p(ans)

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    solve()