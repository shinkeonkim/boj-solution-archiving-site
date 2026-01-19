import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  ret = ""
  for i in s:
    if 'a' <= i <= 'z':
      ret += i
    else:
      ret += " "      
  return ret


def solve():
  n, m = mii()
  a = sorted(mii(), reverse=True)
  b = sorted(mii(), reverse=True)
  
  ans = 0
  for i in range(min(n, m)):
    ans += a[i] * b[i]
  
  p(min(n, m), ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
