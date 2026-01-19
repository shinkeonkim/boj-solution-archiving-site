import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
  

def solve():
  s = [input().split() for _ in range(51)]
  
  d = {}
  for k, v in s:
    v = int(v)
  
    d[k] = d.get(k, 0) + v

    
  for k, v in d.items():
    if v != 91:
      print(k, 91 - v)
    
if __name__ == "__main__":
  tc = 1
  for t in range(tc):
    solve()
    