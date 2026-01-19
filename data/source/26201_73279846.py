import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n = ii()
  s = input()

  crt = 1
  ans = 0

  for i in range(1, n):
    if s[i] == s[i - 1]:
      crt += 1
    else:
      if s[i - 1] == 'a' and crt > 1:
        ans += crt
      crt = 1
  if s[-1] == 'a' and crt > 1:
    ans += crt
  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()