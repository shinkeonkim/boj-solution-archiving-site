import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  l2 = [[], []]
  for i, j in l:
    l2[i].append(j)
  
  l2[0].sort(reverse=True)
  l2[1].sort(reverse=True)

  l = l2[0] + l2[1]
  ans = 0
  for i in range(1, n):
    ans = max(ans, abs(l[i] - l[i - 1]))    
  
  print(ans)
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    