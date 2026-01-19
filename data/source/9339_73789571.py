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


MX = 99999999999999

def solve():
  k = ii()
  numbers = mii()
  
  n = ii()
  
  d = {}
  
  for _ in range(n):
    num, h, s = mii()
    
    if h == s == -1:
      d[num] = MX
    else:
      d[num] = h * 60 + s
  
  l = []
  
  for i in range(k):
    number = numbers[i]
    l.append((d[number], number, i))
  
  l.sort(key = lambda t : (t[0], t[2]))
  
  ans = l[0][1]
  cnt = 0
  for i in l:
    if i[0] <= 360:
      cnt += 1
  
  p(ans, cnt)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
