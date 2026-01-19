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

def f(s, k):
  if len(k) < 4:
    return False
  if s[0] not in k:
    return False
  
  for i in k:
    if i not in s:
      return False
  return True


def solve():
  s = input()
  
  for _ in range(ii()):
    k = input()
    
    if f(s, k):
      p(k)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
