import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def dis(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve():
  n = ii()
  
  l = sorted([mii() for _ in range(n)])
  
  mn = 111111111111
  ans = []
  
  for i in range(n):
    for j in range(i + 1, n):
      if mn > dis(l[i], l[j]):
        mn = dis(l[i], l[j])
        ans = [i, j]
  
  print(*l[ans[0]],*l[ans[1]])
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    solve()

    