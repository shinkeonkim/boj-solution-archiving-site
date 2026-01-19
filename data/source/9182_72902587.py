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
  tc = 1
  while 1:
    a, b, c, d = mii()
    
    if a == b == c == d == -1:
      break

    a %= 23
    b %= 28
    c %= 33
    
    for i in range(1, 1000):
      z = a + 23 * i
      
      if (z - b) % 28 == 0 and (z - c) % 33 == 0:
        p(f"Case {tc}: the next triple peak occurs in {z - d} days.")
        break
    
    tc += 1
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
