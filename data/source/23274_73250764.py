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

MX = 10000000

def point(info, t):
  x = info[0][0] + (info[1][0] - info[0][0]) * t / MX
  y = info[0][1] + (info[1][1] - info[0][1]) * t / MX

  return (x, y)

def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
  
def solve():
  l = mii()
  
  a = [l[:2], l[4:6]]
  b = [l[2:4], l[6:]]
  
  ans = 0
  for t in range(1, MX):
    a_p = point(a, t)
    b_p = point(b, t)
    
    ans = max(ans, dis(a_p, b_p))
  p(sqrt(ans))
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
