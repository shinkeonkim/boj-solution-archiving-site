import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
rng = range

def solve():
  n = ii()
  ans = 0
  for i in range(n // 4 + 1):
    y = n - i * 4
    if y % 5:
      continue
    ans += 1
  print(ans)
  
if __name__ == "__main__":
  tc = 1
  
  for t in rng(tc):
    solve()
    