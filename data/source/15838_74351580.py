import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(stick, per_kg, per_stick):
  a = stick / 85
  return stick * per_stick - per_kg * a - 8 * a

def solve():
  tc = 0
  while 1:
    n = ii()
    tc += 1
    if n == 0:
      break
    
    l = [mii() for _ in range(n)]
    ans = 0
    chicken, beef, lamb, nasi = [0] * 4
    for i in l:
      a, b, c, d = i
      chicken += a
      beef += b
      lamb += c
      nasi += d
      
    ans += f(chicken, 7.5, 0.8)
    ans += f(beef, 24, 1)
    ans += f(lamb, 32, 1.2)
    
    ans += 0.6 * nasi
    
    p(f"Case #{tc}: RM{ans:.2f}")

solve()

# for t in range(1, tc+1):
#   ret = solve()
    