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

def valid_rating(r):
  if r <= 1600:
    return 3
  
  if r <= 1900:
    return 2
  return 1

def is_upper(division, rating):
  if division == 1:
    return False
  
  if division == 2:
    return rating > 1900
  
  return rating > 1600


def solve():
  rating = ii()
  divisions = [*map(int, list(input()))]
  
  v = valid_rating(rating)
  
  if v in divisions:
    p(v)
    return
  
  for division in divisions:
    flag = is_upper(division, rating)
    
    p(division, ("*" if flag else ""), sep="")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   