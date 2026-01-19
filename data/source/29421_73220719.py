import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, g, r = mii() # 녹색불 시간, 빨간불 시간
  l = mii()
  ans = 0
  i = 0
  
  while i < n:
    left = g
    while i < n and l[i] <= left:
      ans += l[i]
      left -= l[i]
      i += 1
    
    if i != n:
      ans += left + r
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
