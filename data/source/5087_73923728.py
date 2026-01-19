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
    
    if s == "#":
      break
    
    l = s.split()[:-1]
    
    cnt = [0, 0]
    
    for idx in range(len(l)):
      i = l[idx]
      if i == 'A':
        i = 1
      else:
        i = int(i)
      
      cnt[i % 2] += 1
    
    if cnt[0] < cnt[1]:
      p("Cheryl")
    elif cnt[0] > cnt[1]:
      p("Tania")
    else:
      p("Draw")
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
