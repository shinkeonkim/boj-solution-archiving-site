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

def f(a, b):
  if len(a) > len(b):
    return False

  if b[:len(a)] == a:
    return True
  
  if b[-len(a):] == a:
    return True
  
  return False
def solve():
  l = [input() for _ in range(3)]
  
  for i in range(3):
    for j in range(3):
      if i == j:
        continue
      
      if f(l[i], l[j]):
        p("No")
        return
  p("Yes")

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    