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


def f(l):
  a, b = l[2] - l[0], l[3] - l[1]
  
  return [min(a, b), max(a, b)]

def g(a, b):
  if a[0] <= b[0] and a[1] <= b[1]:
    return False
  if b[0] <= a[0] and b[1] <= a[1]:
    return False
  return True
  

def solve():
  n = ii()
  l = [f(mii()) for _ in range(n)]
    
  cnt = 0
  for i in range(n):
    for j in range(i + 1, n):
      A = l[i]
      B = l[j]
      
      if g(A, B):
        cnt += 1
  p(cnt)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   