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


def f(s):
  n = len(s)
  ret = ""
  for i in range(n // 2):
    cnt = int(s[2 * i])
    crt = s[2 * i + 1]
    
    ret += crt * cnt
    
  return ret

def solve():
  k, pos = mii()
  s = input()
  
  for _ in range(k):
    s = f(s)
    
  p(s[pos])
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()