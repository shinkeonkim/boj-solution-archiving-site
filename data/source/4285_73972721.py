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
  while 1:
    s = input()
    
    if s == '0':
      break
    k, m = map(int, s.split())
    
    subjects = input().split() # len: k
    chk = True
    for _ in range(m):
      c, r, *l = input().split()
      c = int(c)
      r = int(r)
      
      cnt = 0
      for i in l:
        if i in subjects:
          cnt += 1
      
      if cnt < r:
        chk = False
    
    p("yes" if chk else "no")
      
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
