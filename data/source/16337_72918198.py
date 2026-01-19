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

def solve():
  l = [input() for _ in range(3)]
  
  if l[0] == l[2] == ":::" and l[1] == ":o:":
    return 1
  
  if l[0] == l[2] == "o:o":
    if l[1] == ":::":
      return 4
    if l[1] == ":o:":
      return 5
  
  if l[0] == l[2] == "ooo" and l[1] == ":::":
    return 6
  
  if l[0] == l[1] == l[2] == "o:o":
    return 6
  
  if ((l[0] == "o::" and l[2] =="::o") or (l[0] == "::o" and l[2] =="o::")):
    if l[1] == ":::":
      return 2
    if l[1] == ":o:":
      return 3
  
  return "unknown"
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)