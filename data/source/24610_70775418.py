import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
rng = range

def solve():
  n, m = mii()
  l = [ii() for _ in rng(m)]
  cnt = [0] * m
  
  idx = 0
  
  for _ in range(n):
    for __ in range(2 * m):
      idx %= m
      if cnt[idx] + 1 <= l[idx]:
        cnt[idx] += 1
        idx +=1 
        break
      else:
        idx += 1
  print(*cnt, sep = "\n")
  
if __name__ == "__main__":
  tc = 1
  
  for t in rng(tc):
    solve()
    