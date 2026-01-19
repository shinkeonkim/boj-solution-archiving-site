import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  
  if n == 1:
    p(k)
    return
  
  loop = k // (n + n - 2)
  left = k % (n + n - 2)
  
  cnt = [loop] + [loop * 2] * (n - 2) + [loop]
  
  k = [i for i in range(n)]
  for i in range(n - 2, 0, -1):
    k.append(i)
  for i in k[:left]:
    cnt[i] += 1
  
  p(*cnt)
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
