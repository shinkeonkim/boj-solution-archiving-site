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

def point(d):
  if d > 40000:
    return 0
  
  l = [i * i for i in range(20, 220, 20)]

  for i in range(len(l)):
    if d <= l[i]:
      return 10 - i
  

def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  ans = 0
  for a, b in l:
    d = a * a + b * b
    
    ans += point(d)
  p(ans)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
