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
  n = ii()
  l = [ii() for _ in range(n)]
  
  primes = []
  
  chk = [i for i in range(300)]
  for i in range(2,300):
    if chk[i] == i:
      primes.append(i)
      for j in range(i * i, 300, i):
        chk[j] = 0
  
  s = {}
  
  for i in primes:
    for j in primes:
      s[i + j] = True
  
  for i in l:
    if s.get(i, False):
      p("Yes")
    else:
      p("No")
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()