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

def f(s):
  crt = [310, 420]

  p("300 420 moveto")
  p("310 420 lineto")

  dx = [10, 0, -10, 0]
  dy = [0, -10, 0, 10]
  d = 0

  for i in s:
    if i == "A":
      d += 1
    else:
      d += 3

    crt[0] += dx[d % 4]
    crt[1] += dy[d % 4]

    p(f"{crt[0]} {crt[1]} lineto")
  p("stroke")
  p("showpage")

def solve():
  while 1:
    try:
      s = input()
    except:
      break
    f(s)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()