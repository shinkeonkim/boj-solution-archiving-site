import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  D, C, R = mii()
  
  ans = 0
  
  bad = [ii() for _ in range(C)]
  good = [ii() for _ in range(R)]
  
  i = 0
  j = 0
  
  while i < C and j < R:
    if bad[i] <= D:
      D -= bad[i]
      i += 1
      ans += 1
    else:
      D += good[j]
      j += 1
      ans += 1
  
  while i < C and bad[i] <= D:
    D -= bad[i]
    i += 1
    ans += 1
  
  while j < R:
    j += 1
    ans += 1
    
  print(ans)
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
