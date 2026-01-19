import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  
  p(chr(sum([ord(i) for i in s]) // len(s)))
    

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

