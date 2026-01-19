import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  tc = 0
  while 1:
    tc += 1
    n = ii()

    if n == 0:
      break
    p(f"Machine {tc}")
    energy = [ii() for _ in range(n)]

    while 1:
      name, m = input().split()

      if name == '#' and m == '0':
        break

      sm = 0
      m = int(m)
      l = [mii() for _ in range(m)]

      for level, cnt in l:
        sm += energy[level - 1] * cnt

      p(name, sm)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()