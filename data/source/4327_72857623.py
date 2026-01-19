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

def f(a):
  return a * 9

def anticlockwise(s, e):
  if s < e:
    return f(e - s)
  else:
    return 360 - f(s - e)

def clockwise(s, e):
  if s > e:
    return f(s - e)
  else:
    return 360 - f(e - s)

def solve():
  while 1:
    l = mii()
    if sum(l) == 0:
      break

    ans = 360 * 3

    ans += clockwise(l[0], l[1])
    ans += anticlockwise(l[1], l[2])
    ans += clockwise(l[2], l[3])

    p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()