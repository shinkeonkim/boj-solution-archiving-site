import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  
  sm = 0
  cnt = 0
  
  while 1:
    z = (cnt + 1) ** 2
    
    if sm + z <= n:
      sm += z
      cnt += 1
    else:
      break
  print(cnt)
  
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    