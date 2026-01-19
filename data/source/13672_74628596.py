import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  while 1:
    B, N = mii()

    if B == N == 0:
      break

    money = mii()

    for i in range(N):
      D, C, V = mii() # D: 채무자, C: 채권자

      money[D - 1] -= V
      money[C - 1] += V

    for i in money:
      if i < 0:
        p("N")
        break
    else:
      p("S")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()