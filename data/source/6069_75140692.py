import sys
from math import sqrt, pi, sin, cos, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
prt = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)

def solve():
  n, m = mii()
  queries = [mii() for _ in range(m)]

  stat = [0] * (n + 1)

  for query in queries:
    if query[0] == 0:
      for i in range(query[1], query[2] + 1):
        stat[i] = 1- stat[i]
    else:
      prt(sum(stat[query[1]:query[2]+1]))




if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

