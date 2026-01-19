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
  while 1:
    l = mii()

    if sum(l) == 0:
      break

    cnt = {}

    for i in l:
      cnt[i] = cnt.get(i, 0) + 1

    for i in cnt.values():
      if i % 4 != 0:
        print("no")
        break
    else:
      print("yes")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()