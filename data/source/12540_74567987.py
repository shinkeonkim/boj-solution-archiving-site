import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  money = ii()
  l = mii()

  mn = 0

  ans = (0, 0, 0)

  for i in range(1, 12):
    benefit = (l[i] - l[mn]) * (money // l[mn])

    if benefit > 0:
      if benefit > ans[2]:
        ans = (mn, i, benefit)
      elif benefit == ans[2]:
        if l[ans[0]] > l[mn]:
          ans = (mn, i, benefit)

    if l[i] < l[mn]:
      mn = i

  return ans

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

    if ret == (0, 0, 0):
      p(f"Case #{t}: IMPOSSIBLE")
    else:
      ret = (ret[0] + 1, ret[1] + 1, ret[2])
      p(f"Case #{t}:", *ret)