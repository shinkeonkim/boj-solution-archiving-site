import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  s = inp()
  key = (ord(s[0]) - 97) - (ord(inp()) - 97)
  
  ret = ""
  for i in s:
    ret += chr((ord(i) - 97 - key + 26) % 26 + 97) 
    
  p(ret)


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
