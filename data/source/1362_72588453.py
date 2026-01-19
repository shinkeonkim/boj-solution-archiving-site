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
  tc = 1
  while 1:
    valid, w = mii()

    dead = False

    if valid == w == 0:
      break
    
    while 1:
      action, val = input().split()

      if action == '#':
        break
      
      val = int(val)
      
      if action == 'E':
        w -= val
      else:
        w += val
      
      if w <= 0:
        dead = True
    
    if dead:
      p(tc, "RIP")
    elif valid < w * 2 and w < 2 * valid:
      p(tc, ":-)")
    else:
      p(tc, ":-(")
    tc+=1

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()