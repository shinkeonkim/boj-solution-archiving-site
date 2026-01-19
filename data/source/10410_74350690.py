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
  name, high_date, birthday, course = input().split()
  
  high_date = [*map(int, high_date.split("/"))]
  birthday = [*map(int, birthday.split("/"))]
  
  course = int(course)
  
  if high_date[0] >= 2010:
    return f"{name} eligible"
  
  if birthday[0] >= 1991:
    return f"{name} eligible"
  
  if course >= 41:
    return f"{name} ineligible"
  
  return f"{name} coach petitions"
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
    