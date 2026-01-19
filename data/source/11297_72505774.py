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
    k = sum(l) % 25 + 1
    
    s = input()
    
    for i in s:
      if 'a' <= i <= 'z':
        p(end=chr((ord(i) - 97 - k + 26) % 26 + 97))
      else:
        p(end=i)
    p()
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   