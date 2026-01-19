import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n, k = mii()
  
  l = mii()
  cnt = 0
  
  for i in range(1, n):
    loc = i - 1
    new_item = l[i]
    
    while 0 <= loc and new_item < l[loc]:
      l[loc + 1] = l[loc]
      loc -= 1
      cnt += 1
      
      if cnt == k:
        return l[loc + 1]
    
    if loc + 1 != i:
      l[loc + 1] = new_item
      cnt += 1
      if cnt == k:
        return new_item
  return -1


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)