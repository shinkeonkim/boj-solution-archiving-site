import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = input().split()
  d = {}
  
  for i in l:
    k = i[0]
    
    d[k] = d.get(k, 0) + 1
  
  print(max(d.values()))
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(tc):
    solve()
    