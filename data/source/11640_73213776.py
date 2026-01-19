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
  R, P, D = mii()

  l = [input().split() for _ in range(R)]

  # name, weight, percentage

  scaling = D / P

  primary = 1
  
  for name, weight, percentage in l:
    weight = float(weight)
    percentage = float(percentage)
    
    if percentage == 100:
      primary = weight
  
  primary *= scaling
  
  for name, weight, percentage in l:
    weight = float(weight)
    percentage = float(percentage)
    
    p(name, f"{percentage * primary / 100:.1f}")
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    p(f"Recipe # {t}:")
    ret = solve()
    p("-"*40)