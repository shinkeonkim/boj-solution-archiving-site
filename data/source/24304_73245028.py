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
  n = ii()
  s = input()
  
  crt = ""
  
  l = []
  
  chk = False
  for i in s:
    if '0' <= i <= '9':
      crt += i
    else:
      if len(crt) > 0:
        l.append(crt)
      crt = ""

  if len(crt) > 0:
    l.append(crt)
  
  if len(l) > 0:
    for i in l:
      p(int(i) * n)
  else:
    p("N/A")
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
