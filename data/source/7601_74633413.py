import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, removed):
  if removed == 0:
    return a

  if removed <= a:
    return a + 1
  
  return a


def g(n, b, removed):
  if removed == 0:
    return n - b + 1

  if removed <= b:
    return n - b
  
  return n - b + 1


def solve():
  tc = 0
  while 1:
    n, d = mii()
    tc += 1
    
    if n == d == 0:
      break
    
    p(f"Scenario {tc}")
    becs = ii() # 옷장에서 제거된 의상, 0은 제거 X
    cas = ii()
    
    l = [mii() for _ in range(d)]
    
    for i in range(d):
      a, b = l[i]
      x = f(a, becs)
      y = g(n, b, cas)
      
      p(f"Day {i + 1}", "ALERT" if x == y else "OK")
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    
