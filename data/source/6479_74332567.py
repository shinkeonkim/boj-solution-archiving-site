import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = []
  
  pad = 0
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    l.append(n)
    
    pad = max(pad, len(str(n)))
    inp()

  
  for n in l:
    z = str(factorial(n))
    
    d = {}
  
    for i in range(10):
      d[str(i)] = 0
    
    for i in z:
      d[i] += 1
    
    p(f"{n}! --")
    
    p(BLANK * pad, end = "")
    
    for i in range(5):
      cnt = d[str(i)]
      
      ln = 5 - len(str(cnt))
      
      p(f"({i}){BLANK*ln}{cnt}",end=(BLANK * 4 if i < 4 else BLANK))
    
    p()
    p(BLANK * pad, end = "")
    for i in range(5, 10):
      cnt = d[str(i)]
      
      ln = 5 - len(str(cnt))
      
      p(f"({i}){BLANK*ln}{cnt}",end=(BLANK * 4 if i < 9 else BLANK))
    p()
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
