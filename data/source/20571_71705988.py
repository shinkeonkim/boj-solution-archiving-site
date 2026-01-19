import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  d = {
    "residential": (
      (16, 4),
      (11, 3),
      (6, 2),
      (2, 1),
      (1, 0),
    ),
    "commercial": (
      (15, 3),
      (8, 2),
      (2, 1),
      (1, 0),
    ),
    "industrial": (
      (17, 5),
      (13, 4),
      (9, 3),
      (5, 2),
      (2, 1),
      (1, 0),
    )
  }
  
  s, a = input().split()
  a = int(a)
  
  for f, val in d[s]:
    if f <= a:
      return val
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
