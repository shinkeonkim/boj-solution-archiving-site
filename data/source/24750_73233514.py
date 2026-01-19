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
  A, B, C, D = mii()
  
  flag = False
  for truck in range(0, 1000):
    for boat in range(0, 1000):
      if truck * A >= C + D and boat * B >= max(C, truck * A - D) and max(C, truck * A - D) % B == 0:
        p(f"We need {truck} truck{'' if truck == 1 else 's'} and {boat} boat{'' if boat == 1 else 's'}.")
        flag = True
        break
    if flag:
      break
  else:
    p("No solution.")
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
