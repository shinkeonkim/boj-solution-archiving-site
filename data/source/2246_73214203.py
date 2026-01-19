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
  n = ii()
  l = sorted([mii() + [_] for _ in range(n)], key=lambda t:(t[0], -t[1]))
  
  chk1 = [False] * n
  chk2 = [False] * n
  mn = 1111111111111111
  for i in range(n):
    if mn > l[i][1]:
      chk1[l[i][2]] = True
    mn = min(mn, l[i][1])
  
  l.sort(key=lambda t:(t[1], t[0]))
  
  mn = 1111111111111111
  for i in range(n):
    if mn > l[i][0]:
      chk2[l[i][2]] = True
    mn = min(mn, l[i][0])
  
  cnt = 0
  for i in range(n):
    if chk1[i] and chk2[i]:
      cnt += 1

  p(cnt)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
