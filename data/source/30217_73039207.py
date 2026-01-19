import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  a = input().strip()
  b = input().strip()

  s1 = a[0]
  v1 = ""

  for i in a[1:]:
    if i in "aeiou":
      v1 += i
      break
    s1 += i

  s2 = b[-1]
  v2 = ""

  for i in b[-2::-1]:
    if i in "aeiou":
      v2 += i
      break
    s2 += i

  s2 = s2[::-1]

  o = v2 or v1 or "o"

  p(s1 + o + s2)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()