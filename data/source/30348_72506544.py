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

def f(k):
  if 1 == len(set(str(k))):
    return True
  
  l = [*map(int, list(str(k)))]

  for i in range(1, len(l)):
    if l[i] > l[i - 1]:
      continue
    return False

  return True
  

def solve():
  n = ii()
  ans = []
  
  for i in range(n):
    k = ii()
    
    if f(k):
      ans.append(k)
  
  if len(ans) == 0:
    p("NERASTA")
  else:
    p(min(ans))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   