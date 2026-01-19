import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(num, l):
  for i in str(num):
    if int(i) not in l:
      return False
  return True
  

def solve():
  MX = 100000
  chk = [i for i in range(MX)]
  
  primes = []
  
  chk[0] = chk[1] = -1
  
  for i in range(2, MX):
    if chk[i] == i:
      primes.append(i)
      for j in range(i * i, MX, i):
        chk[j] = -1
  
  n = ii()
  l = mii()
  
  for i in range(MX):
    if chk[i] != -1:
      continue
    if f(i, l):
      p("YES")
      p(i)
      return
  p("NO")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
