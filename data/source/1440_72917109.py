import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def hour(h):
  return 1 <= h <= 12

def minute(m):
  return 0 <= m <= 59

def second(s):
  return 0 <= s <= 59

def solve():
  l = [*map(int, input().split(":"))]
  cnt = 0
  for i in range(3):
    for j in range(3):
      if i == j:
        continue
      k = 3 - (i + j)

      if hour(l[i]) and minute(l[j]) and second(l[k]):
        cnt += 1
  
  p(cnt)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
