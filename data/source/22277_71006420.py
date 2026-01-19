import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l):
  return int(l[0]) * 100 + int(l[1])


def solve():
  n = ii()
  l = [input()[1:].split(".") for _ in range(n + 1)]
  
  k = 0
  k += f(l[0])
  ans = 0
  for i in range(1, n + 1):
    k += f(l[i])
    if k % 100:
      ans += 1
  p(ans)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
