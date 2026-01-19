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

def f(s):
  l = s.split()
  
  score = l[:3]
  name = " ".join(l[3:])
  
  score = [*map(int, score)]
  
  return score + [name]

def solve():
  l = [f(input()) for _ in range(ii())]
  
  l.sort(key = lambda t:(-t[0], -t[1], -t[2]))
  
  p(l[0][3])
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   