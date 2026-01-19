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
  names = [input() for _ in range(ii())]
  
  d = {}
  
  for name in names:
    d[name] = 0
  
  prev = 0
  for _ in range(ii()):
    score, name = input().split()
    
    Z = sum([*map(int, score.split(":"))])
    
    diff = Z - prev
    prev = Z
    
    d[name] += diff
  mx = max(d.values())
  
  for key, val in d.items():
    if val == mx:
      print(key, val)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

