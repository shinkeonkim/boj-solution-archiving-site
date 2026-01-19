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
  s = input().lower()

  place = []

  for i in range(len(s) - 1):
    if s[i] == s[i + 1] == "s":
      place.append(i)

  p(s)
  for i in place:
    print(s[:i] + "B" + s[i + 2:])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()