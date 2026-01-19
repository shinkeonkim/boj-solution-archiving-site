import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  k = ii()
  s = input()
  ans = ""
  for i, c in enumerate(s):
    shift = 3 * (i + 1) + k

    ans += chr((ord(c) - 65 - shift + 26) % 26 + 65)

  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()