import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  
  num = int(s[1:])

  if s[0] == 'R':
    # 6개 
    b = 1 if num <= 36 else 0
    
    if b == 1:
      a = (num - 1) // 4 + 1
    else:
      a = 9 - (num - 37) // 2
    
    c = -1 if num % 2 else 1
    
    p(a,b,c)
  else:
    # 4개    
    if num > 36:
      p(-1)
    else:
      a = (num - 1) // 4 + 1
      b = 1
      c = -1 if num % 2 else 1

      p(a, b, c)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
