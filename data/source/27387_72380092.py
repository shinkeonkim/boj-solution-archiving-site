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
  n, m = mii()
  l = [ii() for _ in range(m)][::-1]
  
  for i in range(1, n + 1):
    crt = i
    
    for leg in l:
      if crt == leg:
        crt = leg + 1
      elif crt == leg + 1:
        crt = leg
    print(crt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

